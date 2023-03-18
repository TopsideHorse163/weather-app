import json
import tkinter
from tkinter import *


def print_intput(input):
    print(input)

def add_location(city, lat, lon):
    new_loc = {
        city: {'LAT': lat, 'LON': lon}
    }
    print(new_loc)

class AddLocation:

    def __init__(self):

        self.window = Tk()

        self.city = tkinter.StringVar()
        self.lat = tkinter.StringVar()
        self.lon = tkinter.StringVar()

        self.city_label = Label(text='Enter City')
        self.city_label.pack(padx=10, pady=10)
        self.city_entry = Entry(self.window, textvariable= self.city)
        self.city_entry.pack(padx=10, pady=10)

        self.lat_label = Label(text='Enter Latitude')
        self.lat_label.pack(padx=10, pady=10)
        self.lat_entry = Entry(self.window)
        self.lat_entry.pack(padx=10, pady=10)

        self.lon_label = Label(text='Enter Longitude')
        self.lon_label.pack(padx=10, pady=10)
        self.lon_entry = Entry(self.window)
        self.lon_entry.pack(padx=10, pady=10)

        self.new_city = self.city.get()
        print(self.new_city)




        # self.submit = Button(text='Submit', command=print_intput(self.new_city))

        self.window.mainloop()



AddLocation()

