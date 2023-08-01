from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_DOWN = 1500
PROMISED_UP = 940

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.down = 0
        self.up = 0
    
    def get_internet_speed(self):
        speed_test_net = "https://www.speedtest.net/"
        self.driver.get(speed_test_net)
        go_button = self.driver.find_element(By.CSS_SELECTOR, "span.start-text")
        go_button.click()
        sleep(45)
        down_speed = self.driver.find_element(By.CSS_SELECTOR, "span.result-data-large.number.result-data-value.download-speed")
        up_speed = self.driver.find_element(By.CSS_SELECTOR, "span.result-data-large.number.result-data-value.upload-speed")
        
        self.down = float(down_speed.text)
        self.up = float(up_speed.text)

        print(self.down, self.up)

    def tweet_at_provider(self, username: str, password: str):
        self.driver.get("https://twitter.com/login")
        sleep(2)

        twitter_email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        twitter_email.send_keys(username)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        next_button.click()
        sleep(2)

        twitter_password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div')
        twitter_password.send_keys(password)
        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        log_in_button.click()
        sleep(5)

        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()

        sleep(3)

        self.driver.quit()