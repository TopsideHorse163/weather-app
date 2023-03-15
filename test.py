import json

import pandas
import requests

LAT = 36.07
LON = -79.79

def api_call():
    api = f'https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true' \
          '&temperature_unit=fahrenheit&daily=temperature_2m_max,temperature_2m_min&timezone=EST'

    response = requests.get(api)
    data = response.json()
    print(json.dumps(data, indent=4))


def asdf():
    wther_code = 3
    data = pandas.read_csv('wmo_weather_codes.csv')
    a = data.condition[wther_code]
    print(a)


# asdf()
api_call()
