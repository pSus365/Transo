# Bus Timetable Display System

This is a simple HTML/CSS/JavaScript web application that displays a digital bus timetable using data from a JSON file. It is designed to run in fullscreen mode on Smart TVs or monitors at a bus station.

## Features

- Fully client-side (no server required)
- Automatically loads timetable data from a JSON file
- Clean and responsive UI optimized for large screens
- Supports automatic scrolling of departures
- Real-time clock displayed in the header
- Easy to update: just modify the `schedule.json` file

## How It Works

1. Timetable data is stored in a local `schedule.json` file.
2. The main HTML page reads the JSON and dynamically generates the timetable table.
3. CSS handles the visual styling.
4. JavaScript updates the clock, scrolls the page, and reloads data if needed.

## Getting Started

To run this system:

1. Clone or download this repository.
2. Open `index.html` in any modern web browser (Chrome recommended).
3. Make sure the `schedule.json` file is located in the same directory.

## Example JSON Format

```json
[
  {
    "destination": "Warsaw",
    "via": "Radom",
    "operator": "BUSTrans",
    "platform": 6,
    "departures": ["8:00 A", "12:20 A", "14:30 A"]
  },
  {
    "destination": "Cracow",
    "via": "Wieliczka",
    "operator": "BusOP",
    "platform": 7,
    "departures": ["5:30 A", "12:20 A"]
  }
]
