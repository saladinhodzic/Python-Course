import os
import requests
import smtplib
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# getting the enviroment variables
load_dotenv()

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,sr;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-67d3ca0d-210b64376bb6d59658d3c76d"}
response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",headers=header)
html = response.text
soup = BeautifulSoup(html,"html.parser")
print(soup.prettify())
whole = soup.select_one(".a-price-whole").getText()
decimal = soup.select_one(".a-price-fraction").getText()
price = float(whole+decimal)
if price < 100:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=os.getenv("SENDER_MAIL"),password=os.getenv("SENDER_PASS"))
        connection.sendmail(from_addr=os.getenv("SENDER_MAIL"),to_addrs=os.getenv("MY_MAIL"),msg="Subject:Alert! Price went down!\n\nThe price of the pot went below 100$")