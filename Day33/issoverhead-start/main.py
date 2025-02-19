import requests
from datetime import datetime
import smtplib
MY_LAT = -30.160314 # Your latitude
MY_LONG = 10.501587 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

my_email = "testingpythoncode321@gmail.com"
password = "wpkj fcii pimv gcfg"
if MY_LAT - 5<= iss_latitude <= MY_LAT+5 and MY_LONG-5 <=iss_longitude<= MY_LONG+5:
        if time_now > sunset or time_now < sunrise:
            with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=my_email,password=password)
                connection.sendmail(from_addr=my_email,to_addrs="hsaladin06@gmail.com",msg="Subject:Look up!\n\n ISS is above you!")



