import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import load_dotenv
import html

load_dotenv(".env.price_tracker")

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_EMAIL_APP_PSWD = os.getenv("SENDER_EMAIL_APP_PSWD")
SMTP = "smtp.gmail.com"
PORT = 587
TO_EMAIL = os.getenv("TO_EMAIL")


product_url = "https://www.amazon.ca/Winsor-Newton-Artists-Water-Color/dp/B000N9964Y/"


request_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6,ja;q=0.5"
}


response = requests.get(product_url, headers=request_header)
product_webpage = response.text

soup = BeautifulSoup(product_webpage, "lxml")

price_str = soup.find(name="span", class_="a-offscreen").text
price_float = float(price_str.split("$")[1])

product_title = soup.find(name="span", id="productTitle").text
product_title = html.unescape(product_title).strip()
# print(product_title)

target_price = 80

### Email Alert
if price_float <= target_price:
    with smtplib.SMTP(host=SMTP, port=PORT) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_APP_PSWD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Amazon Low Price Alert! \n\n{product_title} is now selling at {price_float}!\nBuy at: {product_url}"
        )
    
    print("Email Sent!")
    