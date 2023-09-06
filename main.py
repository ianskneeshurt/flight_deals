from flight_search import FlightSearch
from webdriver import WebDriver
from pprint import pprint

fly_from = "SLC"
fly_to = ["PDX", "SFO", "DTW"]

run_again = True

while run_again:
    ask_again = True
    while ask_again:
        change_flights = input("Change default flights? Y/N: ").upper()
        if change_flights == "Y":
            fly_from = input("Enter Origin Airport Code: ")
            destinations = input("Enter Destination Airport Codes (separated by commas): ")
            fly_to = destinations.split(",")
            ask_again = False
        elif change_flights == "N":
            ask_again = False

    for destination in fly_to:
        flight_prices = FlightSearch(start_airport=fly_from, dest_airport=destination)
        price_data = flight_prices.flight_info()

        if price_data is not None:
            run_again = False
            title = f"Flights from {fly_from} to {destination}"
            print(title)
            pprint(price_data)

            look_up = input("Look up this flight? Y/N: ").upper()
            if look_up == "Y":
                pass
                web_driver = WebDriver()
                web_driver.enter_website(fly_from, destination,
                                         price_data["outbound departure time"], price_data["return departure time"])



