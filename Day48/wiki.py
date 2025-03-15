from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
input = driver.find_element(By.NAME,"fName")
input.send_keys("Saki",Keys.ENTER)
lname = driver.find_element(By.NAME,"lName")
lname.send_keys("Hodza",Keys.ENTER)
email = driver.find_element(By.NAME,"email")
email.send_keys("Saki@gmail.com",Keys.ENTER)
button = driver.find_element(By.CLASS_NAME,'.form-signin button').click()