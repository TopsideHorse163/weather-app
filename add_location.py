import tkinter.messagebox
import requests
from tkinter import *
import json
import ui

FONT = ('Arial', 20, 'bold')
WINDOW_SIZE = '325x470+1000-200'


class AddLocation:

    def __init__(self):
        self.window = Tk()
        self.window.geometry(WINDOW_SIZE)
        self.city_label = Label(text='Enter City', font=FONT)
        self.city_label.grid(row=0, column=0, padx=10, pady=10)

        self.city_entry = Entry(self.window, font=FONT)
        self.city_entry.grid(row=1, column=0, padx=10, pady=10)

        self.submit = Button(text='Submit', command=self.geocode_api_call, font=FONT)
        self.submit.grid(row=6, column=0, padx=10, pady=10)

        self.list_box = Listbox(self.window, selectmode='SINGLE', width=50)
        self.list_box.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.add_button = Button(text='Add', command=self.add_location, font=FONT)
        self.add_button.grid(row=8, column=0, padx=10, pady=10)

        self.window.mainloop()

    def geocode_api_call(self):
        city = self.city_entry.get()
        api = f'https://geocoding-api.open-meteo.com/v1/search?name={city}'
        response = requests.get(api)
        data = response.json()
        search_results = data['results']
        for c in search_results:
            city = c['name']
            state = c['admin1']
            country = c['country_code']
            lat = c['latitude']
            lon = c['longitude']
            result = f'{city}, {state}, {country}, {lat}, {lon}'
            self.list_box.insert("end", result)

    def add_location(self):
        selected_index = self.list_box.curselection()
        selected_city = self.list_box.get(selected_index)
        string_parts = selected_city.split(sep=',')
        city = string_parts[0].strip()
        lat = string_parts[3].strip()
        lon = string_parts[4].strip()
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
        ui.WeatherUi(city)

# AddLocation()
