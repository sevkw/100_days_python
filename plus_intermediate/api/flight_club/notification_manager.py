import os
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib

# load_dotenv(".env.flights")
load_dotenv(r"..\flight_deals\.env.flights")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

FROM_PHONE_NUMBER = os.getenv('FROM_PHONE_NUMBER')
TO_PHONE_NUMBER = os.getenv('TO_PHONE_NUMBER')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_EMAIL_APP_PSWD = os.getenv('SENDER_EMAIL_APP_PSWD')

SMTP = "smtp.gmail.com"
PORT = 587

class NotificationManager:
    """
    This class is responsible for sending notifications with the deal flight details.
    """
    def __init__(self):
        self.account_sid = TWILIO_ACCOUNT_SID
        self.token = TWILIO_AUTH_TOKEN
        self.client = Client(self.account_sid, self.token)
        self.from_number = FROM_PHONE_NUMBER
        self.to_number = TO_PHONE_NUMBER
        self.from_email = SENDER_EMAIL
        self.sender_smtp = SMTP
        self.sender_port = PORT
        self.sender_app_pswd = SENDER_EMAIL_APP_PSWD
    
    def send_message(self, message_body):
        self.client.messages.create(
            body=message_body,
            from_=self.from_number,
            to=self.to_number
        )
    
    def send_emails(self, user_fn:str, user_email:str, message:str):
        """
        To send email to registered users with flight deals found.
        """
        with smtplib.SMTP(self.sender_smtp, port=self.sender_port) as connection:
            connection.starttls()
            connection.login(user=self.from_email, password=self.sender_app_pswd)
            connection.sendmail(
                from_addr=self.from_email, 
                to_addrs=user_email,
                msg=f"Subject: Flight Deals Found for {user_fn}!\n\n{message}",
            )
    
        print("Email Sent!")