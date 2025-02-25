import os
import requests
from twilio.rest import Client

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
API_KEY = os.getenv("WEATHER_API_KEY")
MY_LONGITUDE = 25.501587
MY_LATITUDE = 45.160314
URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={MY_LATITUDE}&lon={MY_LONGITUDE}&appid={API_KEY}&cnt=4"

response = requests.get(URL)
response.raise_for_status()
# get the weather data
data = response.json()

will_rain = False
for day in data["list"]:
    condition_code = day["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(ACCOUNT_SID,AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It's going to rain today.",
            to="+381666666",
            from_="+17623394703"
        )