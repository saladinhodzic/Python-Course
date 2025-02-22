import requests

MY_LONGITUDE = 20.501587
MY_LATITUDE = 43.160314
API_KEY = "bd5e378503939ddaee76f12ad7a97608"
URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={MY_LATITUDE}&lon={MY_LONGITUDE}&appid={API_KEY}&cnt=4"

response = requests.get(URL)
response.raise_for_status()
# get the weather data
data = response.json()
for day in data["list"]:
    if day["weather"][0]["id"] < 800:
        print("Bring an umbrella")