# -------------------------
# Type Conversion & Type Casting in Python
# -------------------------

# Implicit Type Conversion (done automatically by Python)
num_int = 123   # int
num_float = 1.23   # float
sum_result = num_int + num_float
print("Sum:", sum_result)
print("Type of result:", type(sum_result))

# Explicit Type Conversion (type casting)
# int to float
a = 5
b = float(a)
print("Converted int to float:", b)

# float to int
c = 3.9
d = int(c)
print("Converted float to int:", d)

# string to int
str_num = "100"
e = int(str_num)
print("String to int:", e)

# string to float
str_float = "123.45"
f = float(str_float)
print("String to float:", f)

# int to string
g = 77
h = str(g)
print("Int to string:", h, type(h))
