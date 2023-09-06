import requests
from datetime import datetime, timedelta

TEQUILA_KEY = "KqipukB3FHF4xrjEgPMTZfw4aq1f0FHA"
TEQUILA_URL = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self, start_airport, dest_airport):
        now = datetime.now()
        month_ahead = now + timedelta(days=5)
        month_ahead_plus = month_ahead + timedelta(days=30)
        self.fly_from = start_airport
        self.fly_to = dest_airport
        self.date_from = month_ahead.strftime("%d/%m/%Y")
        self.date_to = month_ahead_plus.strftime("%d/%m/%Y")
        self.departure_time = "08:00"
        self.departure_time_end = "19:00"
        self.return_departure_time = self.departure_time
        self.return_departure_end = self.departure_time_end
        self.nights_from = 4
        self.nights_to = 12
        self.max_stops = 0

    def flight_info(self):
        """takes tequila params and returns kiwi api json data for the cheapest flight"""

        header = {"apikey": TEQUILA_KEY}
        parameters = {
            "fly_from": self.fly_from,
            "fly_to": self.fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "nights_in_dst_from": self.nights_from,
            "nights_in_dst_to": self.nights_to,
            "max_stopovers": self.max_stops,
            "dtime_from": self.departure_time,
            "dtime_to": self.departure_time_end,
            "ret_dtime_from": self.return_departure_time,
            "ret_dtime_to": self.return_departure_end,
        }

        response = requests.get(url=TEQUILA_URL, headers=header, params=parameters)

        try:
            price_data = response.json()["data"]
        except KeyError:
            print("Key Error. Double check airport codes")

            return
        else:
            available_index = FlightSearch.available_seat(price_data)
            cheap_flight = price_data[available_index]

            flight_dict = FlightSearch.make_flight_dict(cheap_flight)

        return flight_dict

    @staticmethod
    def available_seat(price_data):
        """takes json data and returns first value of the first index with available seats"""

        available_index = 0
        for index in range(len(price_data)):
            availability = price_data[index]["availability"]["seats"]
            if availability is None or availability < 1:
                pass
            else:
                available_index = index
                break

        return available_index

    @staticmethod
    def make_flight_dict(price_data):
        """takes tequila json for cheapest flight and returns desired values in dictionary"""

        availability = price_data["availability"]["seats"]
        price = price_data["price"]
        duration = price_data["duration"]["total"]
        airlines = str(price_data["airlines"])
        departure_time = price_data["route"][0]["local_departure"]
        return_dept_time = price_data["route"][1]["local_departure"]
        flight_dict = {
            "price": price,
            "duration": duration,
            "availability": availability,
            "airlines": airlines,
            "outbound departure time": departure_time,
            "return departure time": return_dept_time,
        }

        return flight_dict
