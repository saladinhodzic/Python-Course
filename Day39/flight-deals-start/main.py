import requests
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

URL = "https://api.sheety.co/b72a2bb486406ba3a1d6c186930e9930/avioJeftinaPutovanja/prices"
response = requests.get(url=URL)
pprint(response.json())