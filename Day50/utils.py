from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class InternetSpeedBot():
    def __init__(self):
        self.up = 150
        self.down = 10
        self.driver = webdriver.Chrome()
    def get_internet_speed(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach",True)
        self.driver.get("https://www.speedtest.net/")
        self.start = self.driver.find_element(By.CLASS_NAME,"js-start-test").click()
        time.sleep(40)
        self.download = self.driver.find_element(By.CLASS_NAME,"download-speed").text
        self.upload = self.driver.find_element(By.CLASS_NAME,"upload-speed").text
        print(f"Download: {self.download}\nUpload: {self.upload}")
    def tweet(self):
        pass
