##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

from random import choice
import pandas as pd
import datetime as dt
import smtplib

MY_EMAIL = "@gmail.com"
APP_PASSWORD = ""
SMTP = "smtp.gmail.com"
PORT = 587

PLACE_HOLER = "[NAME]"

# get today's info
today = dt.datetime.now()
today_year = today.year
today_month = today.month
today_day = today.day

# randomly choose a letter template and replace the PLACE_HOLDER with bday_name
letter_1 = open(r"letter_templates\letter_1.txt").read()
letter_2 = open(r"letter_templates\letter_2.txt").read()
letter_3 = open(r"letter_templates\letter_3.txt").read()

letter = choice([letter_1, letter_2, letter_3])

# get bday list and see whether there is a match today
bday_file = pd.read_csv("birthdays.csv")
bday_df = pd.DataFrame(bday_file)
try:
    bday_records = bday_df[(bday_df["month"] == today_month) & (bday_df["day"] == today_day)]
    # bday_records = bday_df[(bday_df["year"] == 2020) & (bday_df["month"] == 5) & (bday_df["day"] == 1)]
    bday_name = bday_records.name.values[0]
    bday_email = bday_records.email.values[0]
except IndexError:
    bday_name = None

# check if it is someone's birthday today
if not bday_name is None:
    letter = letter.replace(PLACE_HOLER, bday_name)
    
    # send email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=bday_email,
            msg=f"Subject:Happy Birthday {bday_name}!\n\n{letter}"
        )
    
    print("Email Sent!")
else:
    print("No Birthday!")
