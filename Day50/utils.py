from selenium import webdriver
from selenium.webdriver.common.by import By
class InternetSpeedBot():
    def __init__(self):
        self.up = 150
        self.down = 10
        self.driver = webdriver.Chrome()
    def get_internet_speed(self):
        pass
    def tweet(self):
        pass
speed_bot = InternetSpeedBot()
speed_bot.get_internet_speed()
speed_bot.tweet()