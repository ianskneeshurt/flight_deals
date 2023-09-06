class DataManager:

    def make_flight_dict(self, price_data):
        """takes tequila json for cheapest flight and returns desired values in dictionary"""
        flight_dict = []
        availability = price_data["availability"]["seats"]
        price = price_data["price"]
        duration = price_data["duration"]["total"]
        airlines = str(price_data["airlines"])
        departure_time = price_data["route"][0]["local_departure"]
        return_dept_time = price_data["route"][1]["local_departure"]
        flight_dict.append({"price": price,
                            "duration": duration,
                            "availability": availability,
                            "airlines": airlines,
                            "departure time": departure_time,
                            "return departure time": return_dept_time,
                            })

        return flight_dict
