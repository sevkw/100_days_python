import os
from dotenv import load_dotenv
import requests
from datetime import date, datetime
from flight_data import FlightData
from pprint import pprint


# load_dotenv(".env.flights")
load_dotenv(r"..\flight_deals\.env.flights")

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
    
    def get_price(self, from_city:str, to_city:str):
        """
        First, try price for direct flight.
        if no flights found, check to see if there are flights with 1 stopover.
        """
        date_format = "%d/%m/%Y"
        search_endpoint = f"{self.endpoint}/search"
        depart_date_from = date(2023, 12, 15).strftime(date_format)
        depart_date_to = date(2024, 1, 10).strftime(date_format)
        
        search_param = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_from": depart_date_from,
            "date_to": depart_date_to,
            "nights_in_dst_from": 14,
            "nights_in_dst_to": 21,
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "adults": 1,
            "selected_cabins": "M",
            "curr": "CAD",
            # "price_to": min_price,
            "max_stopovers": 0, ## 0 for direct flight
            "limit": 1
        }
        response = requests.get(url=search_endpoint, headers=self.header, params=search_param)
        response_data = response.json()["data"]
        try:
            data = response_data[0]
            route_data = data["route"][0]
        except IndexError:
            # flight_data = None
            # print(f"No flights found for {to_city}")
            search_param.update({"max_stopovers": 2})
            stpover_response = requests.get(url=search_endpoint, headers=self.header, params=search_param).json()
            stp_over_data = stpover_response["data"][0]
            stp_over_data_route = stp_over_data["route"]
            flight_data = FlightData(
                price=stp_over_data["price"],
                origin_city=stp_over_data_route[0]["cityFrom"],
                destination_city=stp_over_data_route[1]["cityTo"],
                origin_airport=stp_over_data_route[0]["flyFrom"],
                destination_airport=stp_over_data_route[1]["flyTo"],
                departure_date=datetime.fromtimestamp(stp_over_data_route[0]["dTime"]).strftime("%Y-%m-%d"),
                return_date=datetime.fromtimestamp(stp_over_data_route[2]["dTime"]).strftime("%Y-%m-%d"),
                stop_overs=search_param["max_stopovers"] - 1,
                via_city=stp_over_data_route[0]["cityTo"]
            )
            return flight_data
            # pprint(stp_over_data_route)

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=route_data["cityFrom"],
                destination_city=route_data["cityTo"],
                origin_airport=route_data["flyFrom"],
                destination_airport=route_data["flyTo"],
                departure_date=datetime.fromtimestamp(route_data["dTime"]).strftime("%Y-%m-%d"),
                return_date=datetime.fromtimestamp(data["route"][1]["dTime"]).strftime("%Y-%m-%d")
            )
            return flight_data
