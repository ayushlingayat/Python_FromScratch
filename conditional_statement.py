# All Conditional Statement Examples in Python

# 1. if statement
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")

# 2. if-else statement
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3. if-elif-else statement
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# 4. Nested if statement
age = int(input("Enter your age: "))
if age >= 18:
    nationality = input("Are you Indian? (yes/no): ")
    if nationality.lower() == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote in India.")
else:
    print("You are too young to vote.")

# 5. Short-hand if statement
a = 10
b = 5
if a > b: print("a is greater than b")

# 6. Short-hand if-else (ternary operator)
a = 10
b = 20
print("a is greater") if a > b else print("b is greater")

# 7. Logical operators with if
age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")
if age >= 18 and citizen == "yes":
    print("Eligible to vote")
else:
    print("Not eligible to vote")

x = False
if not x:
    print("x is False")


#logical operators
print(not True)
print(not False)