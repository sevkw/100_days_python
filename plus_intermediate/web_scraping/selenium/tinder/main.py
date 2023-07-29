chrome_driver_path = "D:\ChromeDriver\chromedriver.exe"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from time import sleep

import os
from dotenv import load_dotenv

load_dotenv(".env.tinder")
FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
FACEBOOK_PSWD = os.getenv("FACEBOOK_PSWD")

service = Service(r"D:\ChromeDriver\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Visit Tinder and Sign-in using FB account

driver.get("https://tinder.com/")
sleep(2)
# TODO: Click on sign-in button
sign_in_button = driver.find_element(By.CSS_SELECTOR, "a.c1p6lbu0")
# time.sleep(2)
print(sign_in_button.text)
sign_in_button.click()
sleep(2)

# TODO: Login via FB
fb_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Log in with Facebook']")
sleep(2)
fb_button.click()
print("Click Log in with Facebook")
sleep(1)

base_window = driver.window_handles[0]
fb_log_in_window = driver.window_handles[1]
# Switch to FB lg in window
driver.switch_to.window(fb_log_in_window)

sleep(1)
print(driver.title)
# log in and hit enter
email_entry = driver.find_element(By.XPATH, "//*[@id='email']")
pswd_entry = driver.find_element(By.XPATH, "//*[@id='pass']")
# login_button = driver.find_element(By.ID, "loginbutton")

email_entry.send_keys(FACEBOOK_EMAIL)
pswd_entry.send_keys(FACEBOOK_PSWD)
pswd_entry.send_keys(Keys.ENTER)
# login_button.click()


## Switch back to tinder window
driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
sleep(5)

# Pass all pre-settings
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

        ## if only swiping
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.ARROW_RIGHT)
        # actions.perform()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)


