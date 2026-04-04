# Lambda Function Revision
# The syntax of lambda function is there are two syntax

#1) ->  lambda arguments: expression
#2) ->  lamda keyword parameter: operation

#prints square of 2
square = lambda x:x**2
print(square(2))

#prints square of 3
cube = lambda y:y**3
print(cube(3))

#lambda using two parameters

sum_of_two = lambda para1,para2: (para1+para2)
print(sum_of_two(2,4))
#ans should be 6 lets see


#some common things to remember while using the lambda functions

# 1) it should be written in single line
# 2) can have multiple parameters
# 3) have different syntax from regular functions
# -> in lambda functions there are no return statements
# -> lambda functions does not have any name


# -------->




def transform_list(list_nums, function_iterator):
    list_items1 = function_iterator(list_nums[0])
    list_items2 = function_iterator(list_nums[1])
    return [list_items1,list_items2]

def square_1(num):
    return num **2

def cube_1(num):
    return num **3



my_list = [2,4]
print(transform_list(my_list,square_1))
print(transform_list(my_list,cube_1))

#now we can use lambda functions also here output will be
# same but lambda function use kiya


print(transform_list(my_list,square))
print(transform_list(my_list,cube))

#lambda function tab kaam atta jab simple function pass karna hai inside higher order function
# yeeh dekh krr samj sakhte hai hum log



