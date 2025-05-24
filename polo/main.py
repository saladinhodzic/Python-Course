from selenium import webdriver
from selenium.webdriver.common.by import By
from smtplib import SMTP
import os
from dotenv import load_dotenv
load_dotenv('.env')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.polovniautomobili.com/auto-oglasi/pretraga?brand=volkswagen&model%5B%5D=polo&price_to=1900&year_from=2002&year_to=&region%5B%5D=2561&showOldNew=all&submit_1=&without_price=1")

polo_cities = driver.find_elements(By.CLASS_NAME,"city")
for city in polo_cities:
    if city.text == 'Novi Pazar':
        with SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user = os.getenv('SENDER_MAIL'),password=os.getenv("SENDER_PASS"))
            connection.sendmail(from_addr=os.getenv("SENDER_MAIL"),to_addrs=os.getenv("MY_MAIL"),msg="Subject: Polo u Pazaru\n\nPronadjen dobar oglas za polo koji trazis")