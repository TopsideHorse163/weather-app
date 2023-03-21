import requests
import json

"""
I would like to be able to create a city object with the name, state, country, lat, and lon as attributes then pass
these attributes into a list box, then take the selected location from the list box and add it to the locations.json
but am not sure if that will work. I can get the search results to display as strings in the Listbox and I might be able
to parse the string to get the name and lat and lon but I haven't worked out the best way to do that yet.

"""

class CityInfo:

    def __init__(self, city_name):
        api = f'https://geocoding-api.open-meteo.com/v1/search?name={city_name}'
        response = requests.get(api)
        data = response.json()

        search_results = data['results']
        for city in search_results:
            self.city


CityInfo('Greensboro')