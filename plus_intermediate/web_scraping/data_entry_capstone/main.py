from bs4 import BeautifulSoup
from pprint import pprint
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from time import sleep



REAL_ESTATE_LINK = "https://www.royallepage.ca/en/search/homes/on/toronto/?search_str=Bayview+Village%2C+Toronto%2C+ON%2C+CAN&csrfmiddlewaretoken=QSG5h41gYHrAu2gKKQhgmQq09wheN7lughwqDUCFCAvQQlE9AAo4M6PF15LQHT8G&property_type=&house_type=&features=&listing_type=&lat=43.778297&lng=-79.38272&upper_lat=&upper_lng=&lower_lat=&lower_lng=&bypass=&radius=&zoom=&display_type=gallery-view&travel_time=&travel_time_min=30&travel_time_mode=drive&travel_time_congestion=&da_id=&segment_id=&tier2=False&tier2_proximity=0&address=Bayview+Village&method=homes&address_type=neighborhood&city_name=Toronto&prov_code=ON&school_id=&min_price=0&max_price=1200000&min_leaseprice=0&max_leaseprice=5000%2B&beds=2&baths=2&transactionType=SALE&keyword=&sortby="
DATA_ENTRY_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScbMaDueg8303ScpmZS2vljy6qcqfzswNjlvUdjeaMIax_CKg/viewform?usp=sf_link"
CHROME_DRIVER_PATH = r"D:\ChromeDriver\chromedriver.exe"

response = requests.get(REAL_ESTATE_LINK)

soup = BeautifulSoup(response.text, "html.parser")
addresses = soup.find_all(name="address", class_="address-1")


address_list = [address.text.strip() for address in addresses]

prices = soup.select("span.price span")
price_list = [int(price.text.strip().split("$")[-1].replace(",","")) for price in prices if price.text != "$"]

links = soup.select("address.address-1 a")
link_list = [link.get('href') for link in links]

## Fill in form
service = Service(CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


for n in range(len(address_list)):
    driver.get(DATA_ENTRY_FORM_LINK)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address_input.send_keys(address_list[n])
    price_input.send_keys(price_list[n])
    link_input.send_keys(link_list[n])
    submit_button.click()
    sleep(1)
    submit_again_link = driver.find_element(By.LINK_TEXT, "Submit another response")
    # driver.get(submit_again_link)
    submit_again_link.click()

