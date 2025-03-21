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
    for i in range(5):
        inputs = driver.find_elements(By.CSS_SELECTOR,"input[type='text']")
        time.sleep(3)
        address,price,link = inputs
        address.send_keys(addresses[i])
        price.send_keys(prices[i])
        link.send_keys(links[i])
        submit = driver.find_element(By.CSS_SELECTOR,"div[role='button']")
        time.sleep(3)
        submit.click()
        time.sleep(3)
        send_another = driver.find_element(By.CSS_SELECTOR,"a")
        send_another.click()
except Exception as e:
    print(f"Failed to locate tag {e}")