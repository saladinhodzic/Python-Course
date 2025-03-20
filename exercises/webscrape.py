from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# opening the webpage using Selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://practicetestautomation.com/practice-test-login/")
# automate login page
try:
    username = driver.find_element(By.ID,"username")
    username.send_keys("student")
    password = driver.find_element(By.ID,"password")
    password.send_keys("Password123")
    submit = driver.find_element(By.ID,"submit")
    submit.click()
except Exception as e:
    print(f"Failed to login {e}")
