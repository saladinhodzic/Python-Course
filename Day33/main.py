import requests
from datetime import datetime
# LOCATION
MY_LONGITUDE = 20.501587
MY_LATITUDE = 43.160314

# PARAMETERS

parameters = {
    "lat" : MY_LATITUDE,
    "lng" : MY_LONGITUDE,
    "formatted" : 0
}

# GET DATA FROM API

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
# GET OUR CURRENT TIME

time = datetime.now()
print(time)