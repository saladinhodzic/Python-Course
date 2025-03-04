import requests
from flight_search import FlightSearch
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

URL = "https://api.sheety.co/b72a2bb486406ba3a1d6c186930e9930/avioJeftinaPutovanja/prices"
response = requests.get(url=URL)

get_flights = FlightSearch()


sheet_data = response.json()["prices"]