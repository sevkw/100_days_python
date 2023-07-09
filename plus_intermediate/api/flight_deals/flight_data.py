class FlightData:
    """
    This class is responsible for structuring the flight data.
    """
    def __init__(self, price, origin_city, destination_city, origin_airport, destination_airport, departure_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.destination_city = destination_city
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date        
        