import requests
from bs4 import BeautifulSoup
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz
import time

def scrape_vct_schedule(region_name, url, retries=3, delay=5):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            print(f"Successfully fetched data for {region_name}!")
            break  # Exit retry loop if successful
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {region_name} (Attempt {attempt + 1}/{retries}): {e}")
            time.sleep(delay)
    else:
        print(f"Failed to retrieve data for {region_name} after {retries} attempts.")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    matches = []

    for match in soup.select('.wf-module-item.match-item'):  # Match container
        teams = match.select('.match-item-vs-team-name')

        if teams:
            team1 = teams[0].text.strip()
            team2 = teams[1].text.strip() if len(teams) > 1 else "TBD"

            # Placeholder time: All matches set to 12:00 PM UTC (You can edit them in the .ics file)
            placeholder_time = datetime.utcnow().replace(hour=12, minute=0, second=0, microsecond=0, tzinfo=pytz.utc)

            matches.append({
                "team1": team1,
                "team2": team2,
                "time": placeholder_time  # Placeholder time (edit manually later)
            })

    return matches

def create_ical(matches, filename):
    cal = Calendar()
    cal.add('prodid', '-//VCT Schedule//Valorant//EN')
    cal.add('version', '2.0')

    for match in matches:
        event = Event()
        event.add('summary', f"{match['team1']} vs {match['team2']}")
        event.add('dtstart', match['time'])  # Placeholder datetime (change in .ics file)
        event.add('dtend', match['time'] + timedelta(hours=1))  # Assume 1-hour match
        event.add('dtstamp', datetime.now(pytz.utc))
        event.add('description', 'VCT Match (Edit time manually if needed)')
        cal.add_component(event)

    with open(filename, 'wb') as f:
        f.write(cal.to_ical())

    print(f"✅ iCal file created: {filename}")

if __name__ == "__main__":
    regions = {
        "VCT Pacific": "https://www.vlr.gg/event/matches/2379/champions-tour-2025-pacific-stage-1",
        "VCT EMEA": "https://www.vlr.gg/event/matches/2380/champions-tour-2025-emea-stage-1",
        "VCT Americas": "https://www.vlr.gg/event/matches/2347/champions-tour-2025-americas-stage-1",
        "VCT China": "https://www.vlr.gg/event/matches/2359/champions-tour-2025-china-stage-1"
    }

    for region, url in regions.items():
        match_data = scrape_vct_schedule(region, url)
        print(f"\n📌 Scraped {len(match_data)} matches for {region}:")

        if match_data:
            filename = f"vct_{region.lower().replace(' ', '_')}.ics"
            create_ical(match_data, filename)
