# USING SELENIUM FOR WEB SCRAPING
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions().add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org/")
menu = driver.find_elements(By.CSS_SELECTOR,'.event-widget li')
dict = {}
for li in menu:
    key,value = li.text.split("\n")
    dict[key] = value
print(dict)