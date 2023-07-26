chrome_driver_path = "D:\ChromeDriver\chromedriver.exe"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains

service = Service(r"D:\ChromeDriver\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_elements(By.TAG_NAME, "button")[0]

f_name.send_keys("Firstname")
l_name.send_keys("Lastname")
email.send_keys("fname_lname@email.com")
ActionChains(driver).click(button).perform()

status = driver.find_element(By.TAG_NAME, "h1")
print(status.text)

