import os
from dotenv import load_dotenv
import requests


load_dotenv(".env.flights")

FLIGHT_SEARCH_APIKEY = os.getenv("FLIGHT_SEARCH_APIKEY")
FLIGHT_SEARCH_ENDPOINT = os.getenv("FLIGHT_SEARCH_ENDPOINT")


class FlightSearch:
    """This class is responsible for talking to the Flight Search API.
    API reference: https://tequila.kiwi.com/portal/docs/tequila_api
    """
    def __init__(self):
        self.endpoint = FLIGHT_SEARCH_ENDPOINT
        self.header = { "apikey": FLIGHT_SEARCH_APIKEY}
    
    def get_iatacode(self, city_name:str) -> str:
        """Get and return the IATA CODE from City Name"""
        location_endpoint = f"{self.endpoint}/locations/query"
        param = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, headers=self.header, params=param).json()
        iata_code = response["locations"][0]["code"]
        return iata_code
