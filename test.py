import json
import datetime
import pandas
import requests

LAT = 36.07
LON = -79.79

date = datetime.date.today()


# print(date)
def api_call():
    api = f'https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true' \
          '&temperature_unit=fahrenheit&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,' \
          'precipitation_probability_min,precipitation_probability_mean&timezone=EST'

    response = requests.get(api)
    data = response.json()
    print(json.dumps(data, indent=4))
    # today_max = data['daily']['temperature_2m_max'][0]


# print(today_max)


def asdf():
    wther_code = 3
    data = pandas.read_csv('wmo_weather_codes.csv')
    a = data.condition[wther_code]
    print(a)


# asdf()
api_call()
