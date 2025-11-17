class vehicle:
    def __init__(self, brand, model, year):
            self.brand = brand
            self.model = model
            self.year = year

    def start(self):
        print("vehicle is starting")

    def stop(self):
        print("vehicle is stopping")

class Car(vehicle):
    def __init__(self, brand, model, year, num_of_doors, num_of_wheels ):
        super().__init__(brand, model, year)
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels

class Bike(vehicle):
    def __init__(self, brand, model, year, num_of_wheels):
        super().__init__(self, brand, model, year )
        self.num_of_wheels = num_of_wheels

car = Car("ford", "test2", 2026, 4 ,5)
bike = Bike("hunda", "scoopy", 2018, 2)
print(car.__dict__)