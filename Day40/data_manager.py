import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
 
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url="https://api.sheety.co/b72a2bb486406ba3a1d6c186930e9930/avioJeftinaPutovanja/prices")
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

