# Creating Twitter Complaint bot
from utils import InternetSpeedBot
PROMISED_DOWN = 150
PROMISED_UP = 30
speed_bot = InternetSpeedBot()
speed_bot.get_internet_speed()
speed_bot.tweet()