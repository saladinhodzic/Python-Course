from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.polovniautomobili.com/auto-oglasi/pretraga?brand=volkswagen&model%5B%5D=polo&price_to=1900&year_from=2002&year_to=&region%5B%5D=2561&showOldNew=all&submit_1=&without_price=1")