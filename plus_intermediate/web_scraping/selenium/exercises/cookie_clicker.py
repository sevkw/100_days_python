chrome_driver_path = "D:\ChromeDriver\chromedriver.exe"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
import time

service = Service(r"D:\ChromeDriver\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

# timeout = time.time() + 10

# while True:
#     ActionChains(driver).double_click(cookie).perform()
#     if time.time() > timeout:
#         break

# money = driver.find_element(By.ID, "money")
# print(money.text)

store = driver.find_elements(By.CSS_SELECTOR, "#store b")
for i in store:
    print(i.text)