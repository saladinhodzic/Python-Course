from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# opening the webpage using Selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://google.com")
# searching on the google
try:
    textarea = driver.find_element(By.CLASS_NAME,"gLFyf")
    textarea.send_keys("Python Selenium",Keys.ENTER)
except Exception as e:
    print(f"Failed to find textarea object {e}")
