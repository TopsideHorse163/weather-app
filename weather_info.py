import requests
from statistics import mean

""" 

If you want to change the data that you get from the API in the future this is the website
https://open-meteo.com/en/docs#latitude=36.07&longitude=-79.79&hourly=temperature_2m

"""
# a
LAT = 36.07
LON = -79.79


class WeatherInfo:

    def __init__(self):
        api = f'https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true' \
              f'&temperature_unit=fahrenheit&daily=temperature_2m_max,temperature_2m_min&timezone=EST'
        response = requests.get(api)
        data = response.json()

# ----- Data I want to display -----

        # Calculating Today's High
        temp_max_list = data['daily']['temperature_2m_max']
        self.temp_max_avg = round(mean(temp_max_list))

        # Calculating Today's Low
        temp_min_list = data['daily']['temperature_2m_min']
        self.temp_min_avg = round(mean(temp_min_list))

        # Getting Current Temperature and Weather Code
        current_weather = data['current_weather']
        self.current_temp = current_weather['temperature']
        self.current_weathercode = current_weather['weathercode']

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
