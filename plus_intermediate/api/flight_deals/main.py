#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
# pprint(sheet_data)
# pprint(sheet_data[0]['iataCode'])

city_list = []
## update IATA Code for Cities
for data in sheet_data:
    if data["iataCode"] == "":
        city_name = data["city"]
        city_code = flight_search.get_iatacode(city_name)
        data['iataCode'] = city_code
        update_code = {'iataCode' : data['iataCode']}
        row_id = data['id']
        data_manager.update_data(row_id, update_code)
    ## append IATA City codes to a list
    # city_list.append({data['iataCode']:data['lowestPrice']})
    city_list.append(data['iataCode'])

if len(city_list) > 0:
    for city in city_list:
        # to_city = list(city.keys())[0]
        # to_city_low_price = int(list(city.values())[0])
        # search_low_price = flight_search.get_price(to_city, to_city_low_price)
        search_low_price = flight_search.get_price(city)
        print(search_low_price)