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

driver.get("https://www.python.org")
event_names = driver.find_elements(By.XPATH, "//*[@id='content']/div/section/div[2]/div[2]/div/ul/li/a")
## event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
event_times = driver.find_elements(By.XPATH, "//*[@id='content']/div/section/div[2]/div[2]/div/ul/li/time")
## event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

event_list = [event.text for event in event_names]

eventime_list = [time.text for time in event_times]

events = {}

for n in range(len(event_names)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.quit()