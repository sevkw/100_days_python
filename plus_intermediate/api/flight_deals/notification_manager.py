import os
from twilio.rest import Client
from dotenv import load_dotenv
import requests

load_dotenv(".env.flights")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

FROM_PHONE_NUMBER = os.getenv('FROM_PHONE_NUMBER')
TO_PHONE_NUMBER = os.getenv('TO_PHONE_NUMBER')

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
    
    def send_message(self, message_body):
        self.client.messages.create(
            body=message_body,
            from_=self.from_number,
            to=self.to_number
        )
        

    