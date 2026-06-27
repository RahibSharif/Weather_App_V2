import requests

weather_codes = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Heavy Drizzle",
    61: "Light Rain",
    63: "Moderate Rain",
    65: "Heavy Rain",
    71: "Light Snow",
    73: "Moderate Snow",
    75: "Heavy Snow",
    80: "Rain Showers",
    95: "Thunderstorm"
    }

while True:
    print("="*40)
    print("WEATHER REPORT".center(40))
    print("="*40)

    city = input("Enter city name: ").strip().lower()
    
    response = requests.get(
        f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json"
    )

    if response.status_code == 200:
        location = response.json()

        if 'results' not in location:
            print("City not found!")
            print()
            continue

        latitude = location['results'][0]['latitude']
        longitude = location['results'][0]['longitude']

        print()
        print(f"City          : {city.title()}")
        print()
        print(f"Latitude      : {latitude:.2f}")
        print(f"Longitude     : {longitude:.2f}")

        response1 = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=relative_humidity_2m,rain,cloud_cover,is_day,weather_code,temperature_2m,wind_speed_10m"
            )

        weather = response1.json()

        time = weather['current']['time']

        if weather['current']['is_day'] == 1:
            day_status = "Day"
        else:
            day_status = "Night"

        print()
        print(f"Humidity       : {weather['current']['relative_humidity_2m']}%")
        print(f"Rain           : {weather['current']['rain']} mm")
        print(f"Cloud Cover    : {weather['current']['cloud_cover']}%")
        code = weather['current']['weather_code']
        print(f"Weather        : {weather_codes.get(code, 'Unknown')}")
        print(f"Temperature    : {weather['current']['temperature_2m']}°C")
        print(f"Wind Speed     : {weather['current']['wind_speed_10m']} km/h")
        print(f"Time           : {day_status}")
        print(f"Date/Time      : {time}")
        print()

        while True:
            question = input("Search for another city? (y/n): ").lower()

            if question == "y":
                print()
                break
            elif question == "n":
                print()
                print("Goodbye!")
                print()
                exit()
            else:
                print()
                print("You can only enter 'y' or 'n'")
                print()
                continue
    else:
        print("Unable to connect to weather service.")