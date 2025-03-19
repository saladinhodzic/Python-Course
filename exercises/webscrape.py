from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# opening the webpage using Selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://youtube.com")
# searching on the google
try:
    shorts = driver.find_element(By.CSS_SELECTOR,"a[title='Shorts']")
    shorts.click()
    time.sleep(10)
    # returning back to the main page
    driver.back()
except Exception as e:
    print(f"Failed to find textarea object {e}")
