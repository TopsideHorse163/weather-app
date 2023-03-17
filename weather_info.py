import requests
import json

""" 

If you want to change the data that you get from the API in the future this is the website
https://open-meteo.com/en/docs#latitude=36.07&longitude=-79.79&hourly=temperature_2m

"""

# LAT = 36.07
# LON = -79.79
locations = {
    'Greensboro': {'LAT': 36.07, 'LON': -79.79},
    'Radford': {'LAT': 37.13, 'LON': -80.58},
    'Forest': {'LAT': 37.36, 'LON': -79.29}
}


class WeatherInfo:

    def __init__(self, loc):
        print(f'weather_info loc: {loc}')
        LAT = locations[loc]['LAT']
        LON = locations[loc]['LON']
        api = f'https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true' \
              f'&temperature_unit=fahrenheit&daily=temperature_2m_max,temperature_2m_min,' \
              f'precipitation_probability_max,precipitation_probability_min,precipitation_probability_mean&timezone=EST'
        response = requests.get(api)
        data = response.json()
        #print(json.dumps(data, indent=4))
# ----- Data I want to display -----

        # Today's High
        self.todays_max = data['daily']['temperature_2m_max'][0]

        # Today's Low
        self.todays_min = data['daily']['temperature_2m_min'][1]

        # Getting Current Temperature and Weather Code
        current_weather = data['current_weather']
        self.current_temp = current_weather['temperature']
        self.current_weathercode = current_weather['weathercode']

        # Getting Precipitation %
        self.precipitation_max = data['daily']['precipitation_probability_max'][0]
        self.precipitation_min = data['daily']['precipitation_probability_min'][0]
        self.precipitation_mean = data['daily']['precipitation_probability_mean'][0]

# ----- Data I don't want to display -----

        self.latitude = data['latitude']
        self.longitude = data['longitude']
        self.generationtime_ms = data['generationtime_ms']
        self.utc_offset_seconds = data['utc_offset_seconds']
        self.timezone = data['timezone']
        self.timezone_abbreviation = data['timezone_abbreviation']
        self.elevation = data['elevation']
        self.daily_units = data['daily_units']
        self.daily_time = data['daily']['time']
        self.current_windspeed = current_weather['windspeed']
        self.current_winddirection = current_weather['winddirection']

