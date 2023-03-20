from ui import WeatherUi

# from weather_info import WeatherInfo
# from tkinter import *

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

loc = 'Greensboro'
WeatherUi(loc)



