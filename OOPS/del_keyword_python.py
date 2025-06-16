# used to delete object properties or object itself
#del s1.name # to delete properties like this
#del s1 # to delete object like this


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Create object
p1 = Person("Ayush", 22)

# Display info
p1.display()

# Delete an attribute
del p1.age
print("\nAfter deleting age:")

# Try displaying again
try:
    p1.display()
except AttributeError as e:
    print("Error:", e)

# Delete the whole object
del p1

# Try accessing deleted object
try:
    print(p1)
except NameError as e:
    print("Error:", e)
