import requests
# https://www.twilio.com/docs/sms/quickstart/python
import os
from twilio.rest import Client
from dotenv import load_dotenv, dotenv_values


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

stock_params = {
    ## TIME_SERIES_DAILY will need Premium subscription now
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "outputsize":"compact",
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, stock_params)
data = response.json()['Time Series (Daily)']

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_pct = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_pct) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_article_list = [f"{STOCK_NAME}:{up_down}{diff_pct}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    from_phone_number = os.getenv('FROM_PHONE_NUMBER')
    to_phone_number = os.getenv('TO_PHONE_NUMBER')
    for article in formatted_article_list:
        message = client.messages \
                    .create(
                        body=article,
                        from_=from_phone_number,
                        to=to_phone_number
                    )
