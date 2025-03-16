from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
while True:
    driver.find_element(By.ID,"cookie").click()