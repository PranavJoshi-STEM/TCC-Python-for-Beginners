# Classes

class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._mileage = 0 # Protected var
    
    def drive(self, miles):
        self._mileage += miles

    def get_mileage(self):
        return self._mileage


class Car(Vehicle):
    def __init__(self, make, model, year, colour):
        super().__init__(make, model, year)
        self.colour = colour
        self.mileage = 0 # Public var
    
    def display_info(self):
        return f"The car's make, model, year, colour and mileage are: \
{self.make}, {self.model}, {self.year}, {self.colour}, {self.mileage}"
    
    def play_music():
        print('Playing Heat Waves by Glass Animals...')
    
    def drive(self, miles):
        super().drive(miles)
        self.mileage += miles

# Create instance of Vehicle and car
vehicle = Vehicle('Toyota', 'Camry', 2020)
car = Car("Honda", "Accord", 2018, "Red")

# Drive forward
vehicle.drive(100)
car.drive(150)

# mileage
print('Vehicle mileage', vehicle.get_mileage())
print('Car mileage', car.mileage)