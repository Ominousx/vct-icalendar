# VCT iCalendar Generator

## Overview
This repository generates `.ics` calendar files for **VCT 2025** (Valorant Champions Tour) events across different regions. It includes a Python scraper that fetches match schedules from [VLR.gg](https://www.vlr.gg/) and converts them into `.ics` files, making it easy to import matches into Google Calendar, Outlook, or Apple Calendar.

## Files Included
- **`vct_pacific.ics`** – VCT Pacific schedule
- **`vct_emea.ics`** – VCT EMEA schedule
- **`vct_americas.ics`** – VCT Americas schedule
- **`vct_china.ics`** – VCT China schedule
- **`vct_ical_scraper.py`** – Python script to scrape VCT schedules and generate `.ics` files
- **`requirements.txt`** – List of dependencies required to run the scraper

## Installation
To use the scraper, you need Python installed on your system. You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Running the Scraper
To generate `.ics` files from **VLR.gg**, run the following command:

```bash
python vct_ical_scraper.py
```

This will scrape the latest schedules and update the `.ics` files automatically.

## Subscribe to VCT Calendars

Click the links below to add live match schedules to your calendar:

- **[VCT Pacific](https://raw.githubusercontent.com/Ominousx/vct-icalendar/main/vct_pacific.ics)**
- **[VCT EMEA](https://raw.githubusercontent.com/Ominousx/vct-icalendar/main/vct_emea.ics)**
- **[VCT Americas](https://raw.githubusercontent.com/Ominousx/vct-icalendar/main/vct_americas.ics)**
- **[VCT China](https://raw.githubusercontent.com/Ominousx/vct-icalendar/main/vct_china.ics)**

### How to Use
1. **Google Calendar**: Go to Google Calendar → Add Calendar → From URL → Paste the link.
2. **Apple Calendar**: File → New Calendar Subscription → Paste the link.
3. **Outlook**: Add Calendar → Subscribe from Web → Paste the link.

## Contributions
Feel free to open an issue or submit a pull request if you’d like to improve this project!

