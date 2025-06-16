#base class - parent class
class Car:
    color = "black"
    @staticmethod
    def carStarted():
        print("car is started")

    @staticmethod
    def carStoped():
        print("Car is stoped")

#child class inheriting properties of parent class
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name


#object creation karre hum log abb
toyota = ToyotaCar("Fortuner")
print(toyota.name)
toyota.carStarted()
toyota.carStoped()
print(toyota.color)

