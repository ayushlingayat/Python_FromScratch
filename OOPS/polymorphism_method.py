# Base class
class Animal:
    def speak(self):
        print("Animal speaks in a generic way")

# Derived class 1
class Dog(Animal):
    def speak(self):
        print("Dog barks: Woof!")

# Derived class 2
class Cat(Animal):
    def speak(self):
        print("Cat meows: Meow!")

# Polymorphism in action
def animal_sound(animal):
    # This function behaves differently based on the object passed
    animal.speak()

# Creating objects
dog = Dog()
cat = Cat()

# Calling same method, but it behaves differently
animal_sound(dog)  # Output: Dog barks: Woof!
animal_sound(cat)  # Output: Cat meows: Meow!
