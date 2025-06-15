# Encapsulation means wrapping the data (variables) and
# the code (methods) that work on the data into a
# single unit (class),
# and restricting direct access to
# some of the class’s components.

# _single_underscore for
# protected members (a soft rule).
# __double_underscore for private members
# (name mangling).

class Car:
    def __init__(self):
        self.__speed = 0  # private variable

    # Getter method to access private variable
    def get_speed(self):
        return self.__speed

    # Setter method to update private variable
    def set_speed(self, speed):
        if speed > 0:
            self.__speed = speed
        else:
            print("Speed must be positive.")

# Using the Car class
my_car = Car()

# Trying to access private variable directly (not recommended)
# print(my_car.__speed)  # This will give an error

# Proper way using getter and setter
my_car.set_speed(60)
print("Current Speed:", my_car.get_speed())

print("*" * 40)
#Another encapsulation program

class Account:
    def __init__(self, bal, acc):
        self.__balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.__balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.__balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.__balance

acc1 = Account(1000, 12345)
# print(acc1.__balance)  #
acc1.debit(500)
acc1.credit(200)
print(acc1.get_balance())  # ✅ Correct way to access
