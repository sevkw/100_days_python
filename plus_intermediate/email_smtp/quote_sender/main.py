import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "@gmail.com"
# generated by gmail app password
APP_PASSWORD = ""
TO_EMAIL = ""
WEEK_DAY_SEND = 2


with open("quotes.txt") as quote_file:
    quote_list = [line for line in quote_file.readlines()]
    # can just use quote_list = quote_file.readlines(), here just want to practice list comprehension

quote_to_send = choice(quote_list)

week_day = dt.datetime.now().weekday()

if week_day == WEEK_DAY_SEND:

## sent email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=TO_EMAIL,
            msg=f"Subject:Quote of the Week!\n\n{quote_to_send}"
        )
else:
    print(f"No emails to send, but if you want here is a quote: {quote_to_send}")