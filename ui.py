from tkinter import *
from weather_info import WeatherInfo
import pandas

# --- CONSTANTS ---

# (Width)x(Height)+(Left_Right)+(Up_Down)
WINDOW_SIZE = '1000x600+800-150'

FONT = ('Arial', 20, 'bold')
NUM_FONT = ('Arial', 25, 'bold')

COLD_COLOR = '#87CEEB' # Sky Blue
WARM_COLOR = '#FFC000' # Golden Yellow
HOT_COLOR = '#FF2400' # Scarlet

# --- Global Variables ---

weather = WeatherInfo()
max_temp = weather.todays_max
min_temp = weather.todays_min
current_temp = weather.current_temp
current_weathercode = weather.current_weathercode
precipitation_max = weather.precipitation_max
precipitation_min = weather.precipitation_min
precipitation_mean = weather.precipitation_mean

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


def get_weather_conditions():
    # I created the csv file from the weather code key on the API's website
    data = pandas.read_csv('wmo_weather_codes.csv')
    wther_code = weather.current_weathercode
    a = data.condition.values[data['code'] == wther_code]
    return a[0]


def get_weather_icon():
    wc = weather.current_weathercode
    if wc in icon_path_dict:
        wi = icon_path_dict[wc]
        return wi
    else:
        return 'notfound.PNG'


def get_temp_icon():
    ct = weather.current_temp
    if ct < 50:
        return 'coldtemp.PNG'
    elif 50 < ct < 70:
        return 'moderatetemp.PNG'
    else:
        return 'hottemp.PNG'


class WeatherUi:

    def __init__(self):
        # --- Window ---
        self.window = Tk()
        self.window.geometry(WINDOW_SIZE)
        self.window.title('Weather App')

        # --- Labels ---
        self.label_todays_high = Label(text=f"Today's High", font=FONT)
        self.label_todays_high.grid(row=0, column=0, pady=20, padx=20)
        self.label_todays_high_temp = Label(text=f'{max_temp} °F', font=NUM_FONT, fg=num_color(max_temp))
        self.label_todays_high_temp.grid(row=1, column=0, pady=20, padx=20)

        # --- Low Temp for today ---
        self.label_todays_low = Label(text=f"Today's Low", font=FONT)
        self.label_todays_low.grid(row=0, column=1, pady=20, padx=20)
        self.label_todays_low_temp = Label(text=f'{min_temp} °F', font=NUM_FONT, fg=num_color(min_temp))
        self.label_todays_low_temp.grid(row=1, column=1, pady=20, padx=20)

        # --- Current Temperature ---
        self.label_current = Label(text=f'Current Temperature', font=FONT)
        self.label_current.grid(row=2, column=1, pady=20, padx=20)
        self.current_temp_label = Label(text=f'{current_temp} °F', font=NUM_FONT, fg=num_color(current_temp))
        self.current_temp_label.grid(row=3, column=1, pady=20, padx=20)

        # --- Weather Code ---
        self.weather_code_label = Label(text=f'Current Weather code: {current_weathercode}', font=FONT)
        self.weather_code_label.grid(row=2, column=0, pady=20, padx=20)

        # --- Weather Condition ---
        self.weather_condition_label = Label(text=get_weather_conditions(), font=FONT)
        self.weather_condition_label.grid(row=3, column=0, pady=20, padx=20)
        self.weather_condition_label.config(wraplength=200, justify='center')

        # --- Weather Icon ---
        self.weather_icon = PhotoImage(file=f'images/{get_weather_icon()}')
        self.weather_icon_label = Label(image=self.weather_icon)
        self.weather_icon_label.grid(row=4, column=0, pady=20, padx=20)

        # --- Temperature Icon ---
        self.temp_icon = PhotoImage(file=f'images/{get_temp_icon()}')
        self.temp_icon_label = Label(image=self.temp_icon)
        self.temp_icon_label.grid(row=4, column=1, pady=20, padx=20)

        # --- Precipitation Chance ---
        self.rain_chance_label = Label(text='Chance of Rain', font=FONT)
        self.rain_chance_label.grid(row=0, column=2, pady=20, padx=20)
        self.precipitation_max_label = Label(text=f'{precipitation_mean} %', font=NUM_FONT, fg='#0096FF')
        self.precipitation_max_label.grid(row=1, column=2)

        self.window.mainloop()

#WeatherUi()