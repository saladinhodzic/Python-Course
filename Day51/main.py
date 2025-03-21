# Capstone Project using Selenium & BeautifulSoup
from bs4 import BeautifulSoup
import requests
# get the prices, addresses, links using Bs

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
html = response.text
soup = BeautifulSoup(html,"html.parser")
print(soup.prettify())
