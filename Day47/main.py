import requests
from bs4 import BeautifulSoup

response = requests.get("https://appbrewery.github.io/instant_pot/")
html = response.text
soup = BeautifulSoup(html,"html.parser")
price = soup.select_one(".a-price-whole").getText()
decimal = soup.select_one(".a-price-fraction").getText()
print(float(price+decimal))