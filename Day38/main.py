import os
import requests
from datetime import datetime
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key":API_KEY.lstrip("\n")
}

query = input("What exercise you did? ")

response = requests.post(url=URL,json={"query":query},headers=HEADERS)

data = response.json()
duration = data["exercises"][0]['duration_min']
calories = data["exercises"][0]['nf_calories']
exercise = data["exercises"][0]["name"].title()
today = datetime.now().date()
time = datetime.now().time()
# SHEETY API ENDPOINT
sheety_api = "https://api.sheety.co/b72a2bb486406ba3a1d6c186930e9930/vezbanje/workouts"
sheety_headers = {
    "Authorization" : f"Bearer {os.getenv("SHEETY_KEY")}"
}
sheety_data = {
    "workout":
    {
        "date":today.strftime("%d/%m/%Y"),
        "time": time.strftime("%H:%M:%S"),
        "exercise":exercise,
        "duration":duration,
        "calories": calories
    }
}

sheety_response = requests.post(url=sheety_api,json=sheety_data,headers=sheety_headers)
print(sheety_response.text)