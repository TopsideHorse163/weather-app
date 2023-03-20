from weather_info import WeatherInfo
from add_location import AddLocation
from tkinter import *
import tkinter
import pandas
import json

# --- CONSTANTS ---

# (Width)x(Height)+(Left_Right)+(Up_Down)
WINDOW_SIZE = '1000x600+800-150'

FONT = ('Arial', 20, 'bold')
NUM_FONT = ('Arial', 25, 'bold')

COLD_COLOR = '#87CEEB'  # Sky Blue
WARM_COLOR = '#FFC000'  # Golden Yellow
HOT_COLOR = '#FF2400'  # Scarlet

# --- Global Variables ---
# Dictionary pairing weather codes to their corresponding PNG
icon_path_dict = {
    0: 'clearsky.PNG',
    1: 'mainlyclear.PNG',
    2: 'partlycloudy.PNG',
    3: 'overcast.PNG',
    45: 'fog.PNG',
    51: 'drizzlelight.PNG',
    53: 'drizzle.PNG',
    55: 'drizzledense.PNG',
    56: 'freezingrain.PNG',
    57: 'freezingrain.PNG',
    61: 'rainslight.PNG',
    63: 'rainmoderate.PNG',
    65: 'rainheavy.PNG',
    66: 'freezingrain.PNG',
    67: 'freezingrain.PNG',
    71: 'snow.PNG',
    73: 'snow.PNG',
    75: 'snow.PNG',
    77: 'snow.PNG',
    80: 'rainslight.PNG',
    81: 'rainmoderate.PNG',
    82: 'rainheavy.PNG',
    85: 'snow.PNG',
    86: 'snow.PNG',
    95: 'thunderstorm.PNG',
    96: 'thunderstorm.PNG',
    99: 'thunderstorm.PNG',
}

# --- Functions ---


def num_color(num):
    if num < 50:
        return COLD_COLOR
    elif 50 < num < 70:
        return WARM_COLOR
    else:
        return HOT_COLOR


def get_weather_conditions(wther_code):
    # I created the csv file from the weather code key on the APIs website
    data = pandas.read_csv('wmo_weather_codes.csv')
    a = data.condition.values[data['code'] == wther_code]
    return a[0]


def get_weather_icon(wc):
    if wc in icon_path_dict:
        wi = icon_path_dict[wc]
        return wi
    else:
        return 'notfound.PNG'


def get_temp_icon(ct):
    if ct < 50:
        return 'coldtemp.PNG'
    elif 50 < ct < 70:
        return 'moderatetemp.PNG'
    else:
        return 'hottemp.PNG'


def get_locations():
    with open('locations.json', 'r+') as file:
        file_data = json.load(file)
        locations = file_data.keys()
        return locations


class WeatherUi:

    def __init__(self, loc):
        get_locations()
        # print(f' ui loc: {loc}')
        self.weather = WeatherInfo(loc)
        self.max_temp = self.weather.todays_max
        self.min_temp = self.weather.todays_min
        self.current_temp = self.weather.current_temp
        self.current_weathercode = self.weather.current_weathercode
        self.precipitation_max = self.weather.precipitation_max
        self.precipitation_min = self.weather.precipitation_min
        self.precipitation_mean = self.weather.precipitation_mean

        # --- Window ---
        self.window = Tk()
        self.window.geometry(WINDOW_SIZE)
        self.window.title('Weather App')

        # --- Labels ---
        self.label_todays_high = Label(self.window, text=f"Today's High", font=FONT)
        self.label_todays_high.grid(row=0, column=0, pady=20, padx=20)
        self.max_temp_label = Label(self.window, text=f'{self.max_temp} °F', font=NUM_FONT,
                                    fg=num_color(self.max_temp))
        self.max_temp_label.grid(row=1, column=0, pady=20, padx=20)

        # --- Low Temp for today ---
        self.label_todays_low = Label(self.window, text=f"Today's Low", font=FONT)
        self.label_todays_low.grid(row=0, column=1, pady=20, padx=20)
        self.min_temp_label = Label(self.window, text=f'{self.min_temp} °F', font=NUM_FONT,
                                    fg=num_color(self.min_temp))
        self.min_temp_label.grid(row=1, column=1, pady=20, padx=20)

        # --- Current Temperature ---
        self.label_current = Label(self.window, text=f'Current Temperature', font=FONT)
        self.label_current.grid(row=2, column=1, pady=20, padx=20)
        self.current_temp_label = Label(self.window, text=f'{self.current_temp} °F', font=NUM_FONT,
                                        fg=num_color(self.current_temp))
        self.current_temp_label.grid(row=3, column=1, pady=20, padx=20)

        # --- Weather Code ---
        self.current_weathercode_label = Label(self.window, text=f'Current Weather code: {self.current_weathercode}',
                                               font=FONT)
        self.current_weathercode_label.grid(row=2, column=0, pady=20, padx=20)

        # --- Weather Condition ---
        self.weather_condition_label = Label(self.window, text=get_weather_conditions(self.current_weathercode),
                                             font=FONT)
        self.weather_condition_label.grid(row=3, column=0, pady=20, padx=20)
        self.weather_condition_label.config(wraplength=200, justify='center')

        # --- Weather Icon ---
        self.weather_icon = PhotoImage(file=f'images/{get_weather_icon(self.current_weathercode)}')
        self.weather_icon_label = Label(image=self.weather_icon)
        self.weather_icon_label.grid(row=4, column=0, pady=20, padx=20)

        # --- Temperature Icon ---
        self.temp_icon = PhotoImage(file=f'images/{get_temp_icon(self.current_temp)}')
        self.temp_icon_label = Label(self.window, image=self.temp_icon)
        self.temp_icon_label.grid(row=4, column=1, pady=20, padx=20)

        # --- Precipitation Chance ---
        self.rain_chance_label = Label(self.window, text='Chance of Rain', font=FONT)
        self.rain_chance_label.grid(row=0, column=2, pady=20, padx=20)
        self.precipitation_max_label = Label(self.window, text=f'{self.precipitation_mean} %', font=NUM_FONT,
                                             fg='#0096FF')
        self.precipitation_max_label.grid(row=1, column=2)

        # --- Option Menu ---
        self.location_picker_label = Label(self.window, text='Pick a Location', font=FONT)
        self.location_picker_label.grid(row=2, column=2, pady=20, padx=20)

        self.clicked = StringVar()
        self.clicked.set(loc)

        self.drop = OptionMenu(self.window, self.clicked, *get_locations())
        self.drop.config(font=FONT)
        self.drop.grid(row=3, column=2)

        # --- Buttons ---
        self.frame = tkinter.Frame(self.window)
        self.frame.grid(row=4, column=2, pady=20, padx=20)

        self.submit_button = Button(self.frame, text='Submit', command=self.refresh)
        self.submit_button.config(font=FONT)
        self.submit_button.pack(side=tkinter.TOP, pady=10, padx=20)

        self.add_loc_button = Button(self.frame, text='Add Location', command=self.add_location)
        self.add_loc_button.config(font=FONT)
        self.add_loc_button.pack(side=BOTTOM, pady=20, padx=20)

        self.window.mainloop()

    def add_location(self):
        self.window.destroy()
        AddLocation()

    def refresh(self):
        # Get new Location
        new_loc = self.clicked.get()
        self.clicked.set(new_loc)

        # Update the weather variables
        self.weather = WeatherInfo(new_loc)
        self.max_temp = self.weather.todays_max
        self.min_temp = self.weather.todays_min
        self.current_temp = self.weather.current_temp
        self.current_weathercode = self.weather.current_weathercode
        self.precipitation_max = self.weather.precipitation_max
        self.precipitation_min = self.weather.precipitation_min
        self.precipitation_mean = self.weather.precipitation_mean

        # Update Labels with the new weather data
        self.max_temp_label.config(text=f'{self.max_temp}')
        self.min_temp_label.config(text=f'{self.min_temp}')

        self.current_temp_label.config(text=f'{self.current_temp}')
        self.current_weathercode_label.config(text=f'Current Weather code: {self.current_weathercode}')

        self.precipitation_max_label.config(text=self.precipitation_max)
        self.weather_condition_label.config(text=get_weather_conditions(self.current_weathercode))

        # Update the images on the screen
        self.weather_icon.config(file=f'images/{get_weather_icon(self.current_weathercode)}')
        self.weather_icon_label.config(image=self.weather_icon)

        self.temp_icon.config(file=f'images/{get_temp_icon(self.current_temp)}')
        self.temp_icon_label.config(image=self.temp_icon)

# WeatherUi()
