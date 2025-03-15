# USING SELENIUM FOR WEB SCRAPING
from selenium import webdriver
options = webdriver.ChromeOptions().add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://kupujemprodajem.com")