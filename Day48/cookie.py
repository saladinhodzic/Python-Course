from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
start_time = time.time()
end_time = time.time() + 60
while True:
    time.sleep(0.01)
    driver.find_element(By.ID,"cookie").click() 
    current_time = time.time()
    if current_time - start_time >= 5:
        start_time = current_time
        store = driver.find_elements(By.CSS_SELECTOR,"#store div")
        for item in store[::-1]:
            try:
                if "grayed" not in item.get_attribute("class"):
                    item.click()
            except Exception as e:
                print(f"Error {e}")
    if current_time >= end_time:
        cps = driver.find_element(By.ID,"cps").text.split(" : ")[1]
        print(f"You were making {cps} cookies per second!")
        break
driver.quit()