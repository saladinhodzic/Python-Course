import requests
from datetime import datetime,timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

URL = "https://api.sheety.co/b72a2bb486406ba3a1d6c186930e9930/avioJeftinaPutovanja/prices"
response = requests.get(url=URL)
sheet_data = response.json()["prices"]

get_flights = FlightSearch()

city_origin = "LON"

tommorow = datetime.now() + timedelta(days=1)

for city in sheet_data:
    response = get_flights.search_flights(city_origin,city["iataCode"],from_time=tommorow)
    cheapest_flight = find_cheapest_flight(response)
    print(f"Cheapest flight for {city["city"]} is {cheapest_flight.price}")