import requests
from twilio.rest import Client


API_KEY = "bd5e378503939ddaee76f12ad7a97608"
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
            
        )