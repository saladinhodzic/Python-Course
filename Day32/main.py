import smtplib

my_email = "testingpythoncode321@gmail.com"
password = "wpkj fcii pimv gcfg"

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="hsaladin06@gmail.com",msg="Hello World!")
