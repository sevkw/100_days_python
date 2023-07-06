STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "4OYH2F1A20RF5D0Y"
NEWS_API_KEY = "cc3abd46f9da44afb0085ca53d123438"

import requests
# from datetime import date, timedelta

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
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
#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_price = float(daily_stock_data[str(day_before_yesterday)]["4. close"])
# print(day_before_yesterday_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
price_differece = abs(yesterday_close_price - day_before_yesterday_price)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
pct_diff = (price_differece / yesterday_close_price) * 100
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if pct_diff > 5:
    news_response = requests.get(NEWS_ENDPOINT, news_api_params)
    news_data = news_response.json()["articles"]
    news_title_description = [ {article["title"] : article["description"]} for article in news_data ]
    news_len = len(news_title_description)
    # print(news_len)
    for i in range(news_len):
        for t, d in news_title_description[i].items():
            print(f"Headline: {t}")
            print(f"Brief: {d}")
## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

