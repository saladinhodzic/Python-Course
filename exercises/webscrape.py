from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# opening the webpage using Selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://books.toscrape.com/")
# scraping the book titles
try:
    titles = driver.find_elements(By.CSS_SELECTOR,"ol h3 a")
    for title in titles:
        print(title.text)
except Exception as e:
    print(f"Failed to extract titles {e}")
