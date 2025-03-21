# Capstone Project using Selenium & BeautifulSoup
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# get the prices, addresses, links using Bs

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
html = response.text
soup = BeautifulSoup(html,"html.parser")
price_tags = soup.select(".PropertyCardWrapper__StyledPriceLine")
prices = [price.getText().lstrip("$").rstrip("+/mo 1 bd") for price in price_tags]
address_tags = soup.find_all("address")
addresses = [address.getText().strip("\n ") for address in address_tags]
link_tags = soup.select(".StyledPropertyCardDataArea-anchor")
links = [link["href"] for link in link_tags]
# filling the form with this data using Selenium

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://forms.gle/a9o6nW8fGva7GW1Z6")
try:
    inputs = driver.find_elements(By.CSS_SELECTOR,"input[type='text']")
    time.sleep(3)
    address,price,link = inputs
    address.send_keys(addresses[0])
    price.send_keys(prices[0])
    link.send_keys(links[0])
    submit = driver.find_element(By.CSS_SELECTOR,"div[role='button']")
    time.sleep(3)
    submit.click()
except Exception as e:
    print(f"Failed to locate input tag {e}")