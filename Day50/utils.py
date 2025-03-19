from selenium import webdriver
from selenium.webdriver.common.by import By
import time
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
        # self.input = self.driver.find_element(By.CLASS_NAME,"public-DraftStyleDefault-block")