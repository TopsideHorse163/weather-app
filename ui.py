from tkinter import *
from weather_info import WeatherInfo
import pandas

# --- CONSTANTS ---

# WidthxHeight+Left_Right+Up_Down
WINDOW_SIZE = '700x600+1000-150'

FONT = ('Arial', 20, 'bold')
NUM_FONT = ('Arial', 25, 'bold')

COLD_COLOR = '#87CEEB' # Sky Blue
WARM_COLOR = '#FFC000' # Golden Yellow
HOT_COLOR = '#FF2400' # Scarlet

# --- Global Variables ---
weather = WeatherInfo()
temp_max_avg = weather.temp_max_avg
temp_min_avg = weather.temp_min_avg
current_temp = weather.current_temp
current_weathercode = weather.current_weathercode

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

a = 1


def num_color(num):
    if num < 50:
        return COLD_COLOR
    elif 50 < num < 70:
        return WARM_COLOR
    else:
        return HOT_COLOR

# --- Functions ---


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
        self.label_todays_high_temp = Label(text=f'{temp_max_avg} °F', font=NUM_FONT, fg=num_color(temp_max_avg))
        self.label_todays_high_temp.grid(row=1, column=0, pady=20, padx=20)

        # --- Low Temp for today ---
        self.label_todays_low = Label(text=f"Today's Low", font=FONT)
        self.label_todays_low.grid(row=0, column=1, pady=20, padx=20)
        self.label_todays_low_temp = Label(text=f'{temp_min_avg} °F', font=NUM_FONT, fg=num_color(temp_min_avg))
        self.label_todays_low_temp.grid(row=1, column=1, pady=20, padx=20)

        # --- Current Temperature ---
        self.label_current = Label(text=f'Current Temperature', font=FONT)
        self.label_current.grid(row=2, column=1, pady=20, padx=20)
        self.label_current_temp = Label(text=f'{current_temp} °F', font=NUM_FONT, fg=num_color(current_temp))
        self.label_current_temp.grid(row=3, column=1, pady=20, padx=20)

        # --- Weather Code ---
        self.label_weather_code = Label(text=f'Current Weather code: {current_weathercode}', font=FONT)
        self.label_weather_code.grid(row=2, column=0, pady=20, padx=20)

        # --- Weather Condition ---
        self.label_weather_condition = Label(text=get_weather_conditions(), font=FONT)
        self.label_weather_condition.grid(row=3, column=0, pady=20, padx=20)
        self.label_weather_condition.config(wraplength=200, justify='center')

        # --- Weather Icon ---
        self.weather_icon = PhotoImage(file=f'images/{get_weather_icon()}')
        self.label_weather_icon = Label(image=self.weather_icon)
        self.label_weather_icon.grid(row=4, column=0, pady=20, padx=20)

        # --- Temperature Icon ---
        self.temp_icon = PhotoImage(file=f'images/{get_temp_icon()}')
        self.label_temp_icon = Label(image=self.temp_icon)
        self.label_temp_icon.grid(row=4, column=1, pady=20, padx=20)

        self.window.mainloop()
