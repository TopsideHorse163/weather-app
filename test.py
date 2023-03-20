import json
import datetime
import pandas
import requests
from tkinter import *
import json
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


def asdf():
    wther_code = 3
    data = pandas.read_csv('wmo_weather_codes.csv')
    a = data.condition[wther_code]
    print(a)


def option_menu_test():

    with open('locations.json', 'r+') as file:
        file_data = json.load(file)
        new_dict = file_data['city'].keys()
        print(new_dict)

    window = Tk()
    value = StringVar()
    drop = OptionMenu(window, value, *new_dict)
    drop.pack()
    window.mainloop()

# option_menu_test()

