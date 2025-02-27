import os
import datetime as dt
import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey": os.environ.get("API_KEY")
}
response = requests.get("https://www.alphavantage.co/query?",params=parameters)
response.raise_for_status()
data = response.json()

date_now = dt.datetime.now().date()
yesterday = float(data["Time Series (Daily)"][f"2025-02-{date_now.day-2}"]["1. open"])
today = float(data["Time Series (Daily)"][f"2025-02-{date_now.day-1}"]["1. open"])

percentage =round(((today-yesterday)/yesterday)*100,2)

news_parameters = {
    "apiKey":os.environ.get("NEWS_API"),
    "q":COMPANY_NAME,
    "pageSize":4,
    "searchIn":"content",
    "language":"en"
}
if abs(percentage):
    news_response = requests.get("https://newsapi.org/v2/everything",params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    client = Client(os.environ.get("ACCOUNT_SID"),os.environ.get("TWILLIO_TOKEN"))
    message = client.messages \
            .create(to="+381638424288",from_="+17623394703",body=f"TSLA: {percentage}%\n{news_data["articles"][0]["content"]}")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

