# Using Selenium to automate job applying on Linkedin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time
import random
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
submit = driver.find_element(By.XPATH,'//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
submit.click()
time.sleep(2)
easy_apply = driver.find_element(By.CLASS_NAME,"jobs-apply-button")
easy_apply.click()
phone = driver.find_element(By.ID,"single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4175894995-10075439561-phoneNumber-nationalNumber")
phone.send_keys(os.getenv("PHONE"))
next = driver.find_element(By.CSS_SELECTOR,'footer button')
next.click()
next.click()
inputs = driver.find_elements(By.CSS_SELECTOR,"form input")
for input in inputs:
    input.send_keys(str(random.randint(1,3)))
