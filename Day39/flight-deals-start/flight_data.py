class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,origin_airport,destination_airport,from_time):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.from_time = from_time

def find_cheapest_flight(data):
    if data is None or not data["data"]:
        print("No flights")
        return FlightData("N/A","N/A","N/A","N/A")
    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    
    cheapest_flight = FlightData(lowest_price,origin,destination,out_date)
    
    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = float(first_flight["price"]["grandTotal"])
            origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            
            cheapest_flight = FlightData(lowest_price,origin,destination,out_date)
    return cheapest_flight