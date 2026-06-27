# Weather_App_V2

A Python command-line weather application that retrieves real-time weather information using the Open-Meteo APIs.

## Features

- Search weather by city name
- Automatic city geocoding
- Displays latitude and longitude
- Shows current weather conditions
- Displays:
  - Temperature
  - Humidity
  - Rain
  - Cloud cover
  - Wind speed
  - Day/Night status
  - Date and time
- Converts weather codes into readable descriptions
- Handles invalid city names
- Allows searching multiple cities in one session

## Technologies Used

- Python 3
- requests library
- Open-Meteo Geocoding API
- Open-Meteo Weather Forecast API

## Installation

Clone the repository:

```bash
git clone https://github.com/RahibSharif/Weather_App_V2.git
```

Install the required package:

```bash
pip install requests
```

Run the application:

```bash
python main.py
```

## Example Output

```
========================================
            WEATHER REPORT
========================================

Enter city name: Toronto

City: Toronto

Latitude: 43.70643
Longitude: -79.39864

Humidity       : 51%
Rain           : 0.0 mm
Cloud Cover    : 0%
Weather        : Clear Sky
Temperature    : 25.4°C
Wind Speed     : 11.8 km/h
Time           : Day
Date/Time      : 2026-06-27T19:15
```

## Future Improvements

- 7-day weather forecast
- Weather icons
- Air quality information
- Sunrise and sunset times
- Save recent searches
- Graphical user interface (GUI)
