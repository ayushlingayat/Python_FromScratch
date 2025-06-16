# Base class
class Vehicle:
    def show(self):
        print("This is a vehicle")

# Derived class 1
class Car(Vehicle):
    def car_info(self):
        print("Car has 4 wheels")

# Derived class 2
class Bike(Vehicle):
    def bike_info(self):
        print("Bike has 2 wheels")

# Creating objects
c = Car()
b = Bike()
c.show()
c.car_info()
b.show()
b.bike_info()
