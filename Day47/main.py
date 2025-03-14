import os
import requests
import smtplib
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# getting the enviroment variables
load_dotenv()

response = requests.get("https://appbrewery.github.io/instant_pot/")
html = response.text
soup = BeautifulSoup(html,"html.parser")
whole = soup.select_one(".a-price-whole").getText()
decimal = soup.select_one(".a-price-fraction").getText()
price = float(whole+decimal)
if price < 100:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=os.getenv("SENDER_MAIL"),password=os.getenv("SENDER_PASS"))
        connection.sendmail(from_addr=os.getenv("SENDER_MAIL"),to_addrs=os.getenv("MY_MAIL"),msg="Subject:Alert! Price went down!\n\nThe price of the pot went below 100$")