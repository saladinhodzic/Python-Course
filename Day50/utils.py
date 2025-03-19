from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
load_dotenv()
class InternetSpeedBot():
    def __init__(self):
        self.up = 150
        self.down = 10
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=self.options)
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.CLASS_NAME,"js-start-test").click()
        time.sleep(40)
        download = self.driver.find_element(By.CLASS_NAME,"download-speed").text
        upload = self.driver.find_element(By.CLASS_NAME,"upload-speed").text
        print(f"Download: {download}\nUpload: {upload}")
    def tweet(self):
        self.driver.get("https://x.com/home")
        time.sleep(5)
        email = self.driver.find_element(By.CSS_SELECTOR,"input")
        email.send_keys(os.getenv("EMAIL"),Keys.ENTER)
        time.sleep(5)
        user = self.driver.find_element(By.CSS_SELECTOR,"input")
        user.send_keys(os.getenv("USER"),Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_elements(By.CSS_SELECTOR,"input")
        password[1].send_keys(os.getenv("PASSWORD"),Keys.ENTER)
        
        