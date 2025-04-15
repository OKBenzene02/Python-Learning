# Basic class and object
# classes follow a naming convention it should always be a capital letter

class Car:
    def __init__(self, brand, model): # Constructor method is called automatically whenever an object is created.
        self.brand = brand
        self.model = model

    def display(self):
        return f"brand -> {self.brand}\nmodel -> {self.model}"

class ElectricCar(Car):
    def __init__(self, battery_size):
        super().__init__()
        self.battery_size = 10


my_car = Car("BMW", "m3") # object is created (instance)
print()