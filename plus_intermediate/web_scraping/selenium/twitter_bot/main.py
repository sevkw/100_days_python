from bot import InternetSpeedTwitterBot
import os
from dotenv import load_dotenv


CHROME_DRIVER_PATH = r"D:\ChromeDriver\chromedriver.exe"
PROMISED_DOWN_MBPS = 1500
PROMISED_UP_MBPS = 940

load_dotenv()
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

bot.get_internet_speed()

# bot.tweet_at_provider()
