class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.number_passenger = []
        
        
    
    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.number_passenger)

    def pick_up(self, person):
        self.number_passenger.append(person)
        
    def drop_off(self, passenger):
        self.number_passenger.remove(passenger)

    def empty(self):
        self.number_passenger.clear()

    # def pick_up_from_stop(self, bus_stop_1):
    #     pick_up(self, person)
    #     # pick up passenger 
