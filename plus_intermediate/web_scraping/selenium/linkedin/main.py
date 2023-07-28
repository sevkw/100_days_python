chrome_driver_path = "D:\ChromeDriver\chromedriver.exe"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

import time

import os
from dotenv import load_dotenv
import json

load_dotenv(".env.linkedin")
LINKED_IN_EMAIL = os.getenv("LINKED_IN_EMAIL")
LINKED_IN_PSWD = os.getenv("LINKED_IN_PSWD")

service = Service(r"D:\ChromeDriver\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.linkedin.com/jobs/search/?f_JT=F&f_TPR=r604800&f_WT=2&geoId=101174742&keywords=analytics%20engineer&location=Canada&refresh=true&sortBy=DD")

# sign in to linked in
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(1)

# enter email and password
sign_in_email = driver.find_element(By.ID, "username")
sign_in_password = driver.find_element(By.ID, "password")

sign_in_email.send_keys(LINKED_IN_EMAIL)
sign_in_password.send_keys(LINKED_IN_PSWD)
sign_in_password.send_keys(Keys.ENTER)

time.sleep(1)

jobs = driver.find_elements(By.CLASS_NAME, "job-card-container")
time.sleep(2)


# company_list = []
job_titles = []
company_list = []

# for job in jobs:
#     job_text = job.text.splitlines()
#     job_title = job_text[0]
#     company_name = job_text[1]
#     job_titles.append(job_title)
#     company_list.append(company_name)

# follow each company that posted the jobs
for job in jobs[:2]:
    job_id = job.get_attribute("data-job-id")
    print(job_id)
    job_desc = driver.find_element(By.CSS_SELECTOR, f"[data-job-id={job_id}]")
    job_desc.click()
    time.sleep(1)
    # job_desc = driver.get(By.ID, job_id)
    # job.click()
    # time.sleep(1)
    # company_element = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/div/a")
    # company_link = company_element.get_attribute('href')
    # driver.get(company_link)
    # time.sleep(1)
    # follow_button = driver.find_element(By.CSS_SELECTOR, "button.follow")
    # follow_button.click()
    # time.sleep(1)
    # # go back to previous page
    # driver.back()
    # time.sleep(1)


# print(job_titles, company_list)

# job_dict = {}
# for n in range(len(job_titles)):
#     job_dict[n] = {job_titles[n]:company_list[n]}
# print(job_dict)

# with open("jobs.json", "w", encoding="utf-8") as file:
#     json.dump(job_dict, file)





