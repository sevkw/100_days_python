import os
from dotenv import load_dotenv
import requests


# load_dotenv(".env.flights")
load_dotenv(r"..\flight_deals\.env.flights")

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.endpoint = SHEETY_ENDPOINT
        self.token = SHEETY_TOKEN
        self.header = {
            "Authorization": self.token,
        }
    
    def get_data(self):
        """Get and return data from Google Sheet"""
        get_response = requests.get(url=self.endpoint, headers=self.header)
        data = get_response.json()["prices"]
        return data
    
    def update_data(self, row_id, update_dict):
        """Update IATA Code to Google Sheet and returns the put response"""
        put_url = f"{self.endpoint}/{row_id}"
        update_contents = {
            'price': update_dict
        }
        requests.put(url=put_url, headers=self.header, json=update_contents)