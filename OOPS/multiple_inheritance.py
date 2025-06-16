# Parent class 1
class Father:
    def skills(self):
        print("Father: Gardening, Cooking")

# Parent class 2
class Mother:
    def skills(self):
        print("Mother: Painting, Singing")

# Child class inherits from both
class Child(Father, Mother):
    def show(self):
        print("Child has skills from both parents")

# Creating object
c = Child()
c.show()
c.skills()  # From Father due to method resolution order (MRO)
