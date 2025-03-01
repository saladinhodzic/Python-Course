import os
import requests
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key":API_KEY.lstrip("\n")
}

query = input("What exercise you did? ")

response = requests.post(url=URL,json={"query":query},headers=HEADERS)
print(response.json())