import requests
from dotenv import load_dotenv, dotenv_values

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


stock_api_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "outputsize":"compact",
    "datatype":"json",
    "apikey": STOCK_API_KEY
}

news_api_params = {
    "q":COMPANY_NAME,
    "sort_by":"publishedAt",
    "pageSize":3,
    "apiKey":NEWS_API_KEY
    }

stock_response = requests.get(STOCK_ENDPOINT, params=stock_api_params)
stock_response.raise_for_status

daily_stock_data = stock_response.json()['Time Series (Daily)']

stock_dates = list(daily_stock_data.keys())
yesterday = stock_dates[1]
day_before_yesterday = stock_dates[2]

yesterday_close_price = float(daily_stock_data[yesterday]["4. close"])
day_before_yesterday_price = float(daily_stock_data[str(day_before_yesterday)]["4. close"])

price_differece = abs(yesterday_close_price - day_before_yesterday_price)

pct_diff = (price_differece / yesterday_close_price) * 100

if pct_diff > 5:
    news_response = requests.get(NEWS_ENDPOINT, news_api_params)
    news_data = news_response.json()["articles"]
    news_title_description = [ {article["title"] : article["description"]} for article in news_data ]
    news_len = len(news_title_description)

    for i in range(news_len):
        for t, d in news_title_description[i].items():
            print(f"Headline: {t}")
            print(f"Brief: {d}")


