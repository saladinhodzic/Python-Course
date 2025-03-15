from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions().add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
articles = driver.find_element(By.XPATH,'//*[@id="articlecount"]/ul/li[2]/a[1]')
print(articles.text)