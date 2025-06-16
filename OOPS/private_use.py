class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # private variable

    def reset_pass(self):
        print(self.__acc_pass)  # accessing private variable within class

acc1 = Account("12345", "abcde")

print(acc1.acc_no)           # public variable — accessible
# print(acc1.__acc_pass)       #this is private okk through an error
print(acc1.reset_pass())

print("🀄" * 40)

class Person:
    __name = "anonymous"  # private class variable

    def __hello(self):     # private method
        print("hello person!")

    def welcome(self):     # public method
        self.__hello()

p1 = Person()
print(p1.welcome())
