import os
from dotenv import load_dotenv
import requests
load_dotenv()
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("AMADEUS_KEY")
        self.api_secret = os.getenv("API_SECRET")
        self.token = self.get_new_token()
    
    def get_new_token(self):
        self.headers = {
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        self.body = {
            "grant_type" : "client_credentials",
            "client_id" : self.api_key,
            "client_secret" : self.api_secret
        }
        
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token",headers=self.headers,data=self.body)
        return response.json()["access_token"]