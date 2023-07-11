#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

from pprint import pprint

ORIGIN_CITY_IATA = "YTO"

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
notifier = NotificationManager()

## update IATA Code for Cities
for data in sheet_data:
    if data["iataCode"] == "":
        city_name = data["city"]
        city_code = flight_search.get_iatacode(city_name)
        data['iataCode'] = city_code
        update_code = {'iataCode' : data['iataCode']}
        row_id = data['id']
        data_manager.update_data(row_id, update_code)

for destination in sheet_data:
    flight_data = flight_search.get_price(from_city=ORIGIN_CITY_IATA, to_city=destination["iataCode"])
    if flight_data.price < destination["lowestPrice"]:
        message = f"Low price alert! Only ${flight_data.price} from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.departure_date} to {flight_data.return_date}."
        if flight_data.stop_overs > 0:
            print(message)
            stop_over_msg = f"Flight has {flight_data.stop_overs} stop over, via {flight_data.via_city}."
            print(stop_over_msg)
            email_message = "\n" + message + "\n" + stop_over_msg
        else:
            print(message)
            email_message = email_message + message

# Send email to registered users if there are any users
users_list = data_manager.get_users()
if len(users_list) > 0:
    for user in users_list:
        user_fn = user["firstName"]
        user_email = user["email"]
        notifier.send_emails(user_fn=user_fn, user_email=user_email, message=email_message)
