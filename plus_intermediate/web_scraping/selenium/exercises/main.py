## Useful reference: https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python

chrome_driver_path = "D:\ChromeDriver\chromedriver.exe"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"D:\ChromeDriver\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# driver.get("https://www.amazon.ca/Winsor-Newton-Artists-Water-Color/dp/B000N9964Y/")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

# driver.get("https://www.python.org")
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text) 

driver.quit()