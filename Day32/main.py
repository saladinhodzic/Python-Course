import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

my_email = "testingpythoncode321@gmail.com"
password = "wpkj fcii pimv gcfg"

with open("quotes.txt") as quotes:
    data = quotes.readlines()
    random_quote = random.choice(data)

if weekday == 3:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="hsaladin06@gmail.com",msg=random_quote)
