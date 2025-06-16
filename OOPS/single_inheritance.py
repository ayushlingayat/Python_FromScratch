# Parent class
class Animal:
    def speak(self):
        print("Animals can speak")

# Child class inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating object
d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Defined in Dog
