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
- As of 3-22-23 This program is mostly complete, I cannot think of anything else to add other than improving the look
of the overall UI or adding more weather information. The information being displayed currently is the only information
that I understand and find useful. 
- 3-24-23: I added the ability to search for a location using open meteo's geocoding api. Now when you go to add a
location you can just type in the name of the city and it will give a list of results that you can pick from, the
program will then add that location to the locations.json file and reopen the ui with the newly added city.
"""

loc = 'Greensboro'
WeatherUi(loc)



