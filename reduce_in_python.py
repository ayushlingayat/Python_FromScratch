#so Reduce koo import karna hota hee first use karne kee liye

# SYNTAX for reduce
# reduce(function,iterable)


from functools import reduce

numbers_list = [1,1,3,4,6,7,9]


reduced_var = reduce(lambda x,y: x+y, numbers_list)

print(reduced_var)
#reduce ek single value return karta hai
# iterable nhi so list lagane kii jarurat nhi


