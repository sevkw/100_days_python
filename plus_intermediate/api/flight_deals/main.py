#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
# pprint(sheet_data)
# pprint(sheet_data[0]['iataCode'])

for data in sheet_data:
    if data["iataCode"] == "":
        city_name = data["city"]
        city_code = flight_search.get_iatacode(city_name)
        data['iataCode'] = city_code
        update_code = {'iataCode' : data['iataCode']}
        row_id = data['id']
        data_manager.update_data(row_id, update_code)
