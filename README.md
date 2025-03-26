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

## How to Use `.ics` Files
You can import these `.ics` files into:
- **Google Calendar**: [Guide](https://support.google.com/calendar/answer/37118?hl=en)
- **Apple Calendar**: [Guide](https://support.apple.com/guide/calendar/import-or-export-calendars-icl1022/mac)
- **Outlook Calendar**: [Guide](https://support.microsoft.com/en-us/office/import-or-subscribe-to-a-calendar-in-outlook-on-the-web-503ffaf6-7b86-44fe-8dd6-8099d95f38df)

## Contributions
Feel free to open an issue or submit a pull request if you’d like to improve this project!

