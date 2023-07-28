chrome_driver_path = "D:\ChromeDriver\chromedriver.exe"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service = Service(r"D:\ChromeDriver\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

start_time = time.time()
timeout = start_time + 60*5
time_to_buy = start_time + 5

while True:
    cookie.click()
    store = driver.find_elements(By.CSS_SELECTOR, "#store b")
    store_dict = {i.text.split(" - ")[-1].replace(',', ''): i for i in store}
    del store_dict['']
    store_dict = {int(k):v for k, v in store_dict.items()}
    buyable = []

    if time.time() > time_to_buy:
        money = int(driver.find_element(By.ID, "money").text)
        print(money)
        for key, value in store_dict.items():
            if money > key:
                buyable.append(key)
        to_buy = max(buyable)
        item_to_buy = store_dict[to_buy]
        item_to_buy.click()
        print(item_to_buy)
        print("Item Bought")
    
        time_to_buy = time.time() + 3

    if time.time() > timeout:
        break