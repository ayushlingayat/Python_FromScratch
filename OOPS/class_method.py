class Person:
    # Class variable (shared across all instances)
    name = "anonymous"

    # Class method to change the class variable 'name'
    @classmethod
    def changeName(cls, name):
        cls.name = name  # Changes the class-level 'name' attribute


# Creating an object of Person
p1 = Person()

# Changing class variable using the object
p1.changeName("rahul kumar")

# Accessing the updated class variable through object and class
print(p1.name)        # Output: rahul kumar
print(Person.name)    # Output: rahul kumar
