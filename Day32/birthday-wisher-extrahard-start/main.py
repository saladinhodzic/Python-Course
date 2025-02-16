##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
# 1. Update the birthdays.csv

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict("records")

# 2. Check if today matches a birthday in the birthdays.csv

today_date= dt.datetime.now()
for dict in data_dict:
    if today_date.month == dict["month"] and today_date.day == dict["day"]:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            birthday_wish = ""
            for line in letter:
                new_line = line.replace("[NAME]",dict["name"])
                birthday_wish+=new_line
            my_email = "testingpythoncode321@gmail.com"
            password = "qrmu qvre qssj xeqq"
            with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=my_email,password=password)
                connection.sendmail(from_addr=my_email,to_addrs=f"{dict["email"]}",msg=birthday_wish)
# if today_date

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




