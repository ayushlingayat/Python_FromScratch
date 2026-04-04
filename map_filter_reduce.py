#this is important concept as per data field

def cube(num):
    return num **3

cube_fun = lambda y:y**3

list_demo = [1,2,3,4,5,6,7,8]
em_list = []

for elem in list_demo:
    em_list.append(cube_fun(elem))

print("The appended cube of list is : ",em_list)

# ======================================MAP=====================================
# The syntax of map is :
# map(function, iterable)

square_fun = lambda x: x**2
my_list = [2,4,6,8,10]

#using map here okk see carefully
new_list = map(square_fun,my_list)
print(new_list) #aesha print kiya toh object dega vooh usko list
#mein convert krr lena

print(list(new_list))

#directly using lambda function iss baar cube print karra

neww_list = map(lambda x:x**3,my_list)
print(list(neww_list))

# map mein app function kaa naam dedo phir dedo vooh list jismein aap
# yeeh apply karna chahate hoo that's it

# ===========================================FILTER=====================================

# filter() function is used to extract elements
# from an iterable (like a list, tuple or set)
# that satisfy a given condition.
# It works by applying a function to each element
# and keeping only those for which function returns True.


# ==> SYNTAX:
# filter(function,iterable_list)
# joo value filter kee true honge vooh show honge false vale show nhi hote


def filter_fun(a):
    return a > 4

mynew_filter = filter(filter_fun,my_list)
print(list(mynew_filter))



