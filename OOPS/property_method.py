class Student:
    # Constructor to initialize subject marks
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    # Property to calculate percentage
    @property
    def percentage(self):
        # Calculates average and returns as string with a "%" symbol
        return str((self.phy + self.chem + self.math) / 3) + "%"


# Creating a student object with marks
stu1 = Student(98, 97, 99)

# Accessing percentage like an attribute (not method)
print(stu1.percentage)  # Output: 98.0%

# Updating one subject's mark
stu1.phy = 86

# Accessing updated percentage
print(stu1.percentage)  # Output will reflect the updated value