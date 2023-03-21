import tkinter.messagebox
import requests
from tkinter import *
import json
import ui

FONT = ('Arial', 20, 'bold')




class AddLocation:

    def __init__(self):
        self.window = Tk()

        self.city_label = Label(text='Enter City', font=FONT)
        self.city_label.grid(row=0, column=0, padx=10, pady=10)

        self.city_entry = Entry(self.window, font=FONT)
        self.city_entry.grid(row=1, column=0, padx=10, pady=10)

        # self.lat_label = Label(text='Enter Latitude', font=FONT)
        # self.lat_label.grid(row=2, column=0, padx=10, pady=10)
        #
        # self.lat_entry = Entry(self.window, font=FONT)
        # self.lat_entry.grid(row=3, column=0, padx=10, pady=10)
        #
        # self.lon_label = Label(text='Enter Longitude', font=FONT)
        # self.lon_label.grid(row=4, column=0, padx=10, pady=10)
        #
        # self.lon_entry = Entry(self.window, font=FONT)
        # self.lon_entry.grid(row=5, column=0, padx=10, pady=10)

        self.submit = Button(text='Submit', command=self.geocode_api_call, font=FONT)
        self.submit.grid(row=6, column=0, padx=10, pady=10)

        self.list_box = Listbox(self.window, selectmode='SINGLE', width=50)
        self.list_box.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.window.mainloop()

# I am not sure if I will do everything from methods like this or if I will use city_info.py to do this. Longer comment
    # in city_info.py
    def geocode_api_call(self):
        city = self.city_entry.get()
        api = f'https://geocoding-api.open-meteo.com/v1/search?name={city}'

        response = requests.get(api)
        data = response.json()
        search_results = data['results']
        options_list = []
        for c in search_results:
            city = c['name']
            state = c['admin1']
            country = c['country_code']
            lat = c['latitude']
            lon = c['longitude']
            result = f'{city}, {state}, {country}, {lat}, {lon}'
            self.list_box.insert("end", result)
            # options_list.append(result)


    def add_location(self):
        city = self.city_entry.get()
        lat = 1#self.lat_entry.get()
        lon = 2#self.lon_entry.get()
        new_location = {
            city: {"LAT": lat, "LON": lon}
        }

        with open('locations.json', 'r+') as file:
            # Load data into dictionary
            file_data = json.load(file)
            # Add new location to old data dictionary
            file_data.update(new_location)
            # Sets file's current position at offset.
            file.seek(0)
            # Convert dictionary back to json.
            json.dump(file_data, file, indent=4)

        tkinter.messagebox.showinfo(title='Location Added', message='Location Added')
        self.window.destroy()
        #ui.WeatherUi(city)


# class CityInfo:
#
#     def __init__(self, results_json):
#         search_results = results_json['results']
#         self.options_list = []
#         for c in search_results:
#             city = c['name']
#             state = c['admin1']
#             country = c['country_code']
#             lat = c['latitude']
#             lon = c['longitude']
#             result = f'{city}, {state}, {country}, {lat}, {lon}'
#             self.options_list.append(result)


AddLocation()
