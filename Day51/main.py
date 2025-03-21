# Capstone Project using Selenium & BeautifulSoup
from bs4 import BeautifulSoup
import requests
# get the prices, addresses, links using Bs

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
html = response.text
soup = BeautifulSoup(html,"html.parser")
price_tags = soup.select(".PropertyCardWrapper__StyledPriceLine")
prices = [price.getText().lstrip("$").rstrip("+/mo 1 bd") for price in price_tags]
address_tags = soup.find_all("address")
addresses = [address.getText().strip("\n ") for address in address_tags]
print(addresses)