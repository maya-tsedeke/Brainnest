
"""Create a Vehicle class with the following attributes: make, model, and year. The class should also have the following
methods: start(), stop(), and info().

Create a Car class that inherits from the Vehicle class. The Car class should have an additional attribute: num_doors.
The class should also have the following method: lock_doors()."""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.running = False

    def start(self):
        if self.running:
            print("The vehicle is already running.")
        else:
            self.running = True
            print("The vehicle has started.")

    def stop(self):
        if not self.running:
            print("The vehicle is already stopped.")
        else:
            self.running = False
            print("The vehicle has stopped.")

    def info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nRunning: {self.running}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def lock_doors(self):
        print("Doors are locked.")

# Example usage
my_vehicle = Vehicle("Toyota", "Camry", 2022)
my_vehicle.start()  # prints "The vehicle has started."
my_vehicle.info()   # prints the vehicle's info including running status

my_car = Car("BMW", "M3", 2023, 4)
my_car.start()      # prints "The vehicle has started."
my_car.lock_doors() # prints "Doors are locked."
my_car.info()       # prints the car's info including running status and number of doors

