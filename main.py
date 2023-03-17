from ui import WeatherUi
from weather_info import WeatherInfo
from tkinter import *

"""
- I am going to create my own rain alert type program here. OpenWeather changed their API TOS, and I was not sure how to
get it to work properly so, I am going to try to use Open-meteo.com instead.

- https://open-meteo.com/en/docs#latitude=36.07&longitude=-79.79&hourly=temperature_2m This is the website I used
- As of 3-14-23 I have the gui and the api call working so, I can see the weather information I want. I might add a
way to text me the weather at a certain time of day which is what the normal project would be doing.
- I wrote a batch file the will cd into the rain-alert directory and run the main.py file, this lets me run this from
my desktop.
- Also, might try and write the same program in Java just to try it. I have no idea how to make API calls in Java
"""


# locations = ['Greensboro', 'Radford', 'Forest']
# window = Tk()
# window.geometry('200x200+1350-450')
# window.title('Pick a Location')
#
# Label(text='Pick a location').pack()
#
# clicked = StringVar()
# clicked.set(locations[0])
#
# OptionMenu(window, clicked, *locations).pack()
#
# loc = ''
# print(f'main loc 1: {loc}')
#
#
# def set_location():
#     global loc
#     loc = clicked.get()
#     print(f'set_location loc: {loc}')
#     window.quit()
#
#
# def close():
#     window.destroy()
#
#
# Button(text='Submit', command=lambda: [set_location(), close()]).pack()
#
# window.mainloop()
# print(f'main loc 2: {loc}')
loc = 'Greensboro'
WeatherUi(loc)
