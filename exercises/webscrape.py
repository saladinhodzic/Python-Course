from selenium import webdriver
# opening the webpage using Selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://google.com")
