# Using Selenium to automate job applying on Linkedin
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
load_dotenv()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4175894995&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
sign_in = driver.find_element(By.CSS_SELECTOR,".sign-in-modal button")
sign_in.click()
email = driver.find_element(By.ID,"base-sign-in-modal_session_key")
email.send_keys(os.getenv("EMAIL"))
password = driver.find_element(By.ID,"base-sign-in-modal_session_password")
password.send_keys(os.getenv("PASS"))
submit = driver.find_element(By.CLASS_NAME,"sign-in-form__submit-btn--full-width")
submit.click()