## below is the answer code from Angela Yu's video
## video link: https://www.udemy.com/course/100-days-of-code/learn/lecture/21110118?start=0#overview

import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = "@gmail.com"
APP_PASSWORD = ""
SMTP = "smtp.gmail.com"
PORT = 587

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today = (today_month, today_day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(SMTP, port=PORT) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday! \n\n{contents}"
        )
