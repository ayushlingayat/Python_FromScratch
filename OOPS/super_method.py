# super().__init__(type) is used to call the parent class constructor.
# It ensures that the type attribute (defined in Car) gets properly initialized.
# Without super(), the parent class (Car)’s __init__ method won't be called, and self.type won't exist unless you manually set it again.
# This helps in code reuse and avoids duplicating code in child classes.


# Base class
class Car:
    def __init__(self, type):
        # Initializing 'type' attribute for car
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")


# Derived class inheriting from Car
class ToyotaCar(Car):
    def __init__(self, name, type):
        # Calling parent class constructor using super()
        # This initializes the 'type' attribute from the Car class
        super().__init__(type)
        super().start()
        super().stop()


        # Now initialize the 'name' attribute for ToyotaCar
        self.name = name


# Creating an object of ToyotaCar with name and type
car1 = ToyotaCar("prius", "electric")

# Accessing inherited property from Car class
print(car1.type)

