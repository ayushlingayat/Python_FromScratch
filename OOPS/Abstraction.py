# Abstraction means hiding complex details and
# showing only the necessary things.
# In Python, we achieve it using abstract classes
# and abstract methods.

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#
#     def carStart(self):
#         self.clutch = False
#         self.acc = False
#         print("Car Started")
#
# car1 = Car()
# car1.carStart()


from abc import ABC, abstractmethod

# Abstract class
class Car(ABC):

    # Abstract method
    @abstractmethod
    def start(self):
        pass

    # Concrete method (normal method)
    def stop(self):
        print("Car has stopped.")

# Child class
class Tesla(Car):
    def start(self):
        print("Tesla is starting silently with electricity.")

# Using the class
my_car = Tesla()
my_car.start()
my_car.stop()
