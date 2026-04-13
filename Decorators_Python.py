# Decorators in python

# A decorator is a function that wraps another
# function to extend or modify its behavior
# without changing the original function
# It uses the @ syntax and follows the concept of
# higher-order functions

def decorator_func(func):
    def wrapper():
        print("Before the func it will execute")
        func()
        print("after the func it will execute")
    return wrapper


@decorator_func
def say_hello():
    print("Hello i am ayush")

decorator_print = decorator_func(say_hello)
print(decorator_print)

# Decorator with Arguments (*args, **kwargs)
# Essential for decorating any function regardless of
# its parameters

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Function returned: {result}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

add(3, 5)
# Output:
# Calling add with args=(3, 5), kwargs={}
# Function returned: 8


