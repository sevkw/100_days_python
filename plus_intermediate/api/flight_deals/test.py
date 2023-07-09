from pprint import pprint
from flight_search import FlightSearch

flightsearch = FlightSearch()
pprint(flightsearch.get_price(from_city="YTO", to_city="TPE"))