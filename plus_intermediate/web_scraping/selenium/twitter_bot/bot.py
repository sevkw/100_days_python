from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep



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

    def tweet_at_provider(self):
        pass
