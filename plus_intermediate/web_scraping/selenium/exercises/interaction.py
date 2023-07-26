chrome_driver_path = "D:\ChromeDriver\chromedriver.exe"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

service = Service(r"D:\ChromeDriver\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()
# print(article_count.text)

# content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
content_portals = driver.find_element(By.XPATH, "//*[@id='mp-other-content']/ul/li[7]/b/a")
# print(content_portals.text)
# content_portals.click()

search = driver.find_element(By.NAME, "search")
# type 'Python' into search bar
search.send_keys("Python")
# hit enter key
# https://www.selenium.dev/documentation/webdriver/actions_api/keyboard/#keys
search.send_keys(Keys.ENTER)