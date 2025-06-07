def calSum(a,b):
    sum = a+b
    return sum

fun_Call = calSum(2,3)

print(fun_Call)

def printhello():
    return print("Hello")

printing = printhello()

print(printing)

#joo function khuch bhi return nhi karta usmein null value atti
#automatically just remember that

def avg_number(a,b,c):
    avg = a+b+c / 3
    return avg

avg_num = avg_number(99 , 87, 78)

print(avg_num)


#default parameter

#default argument humesha piche hee dena okk
def defa_param(d ,e , f =12):
    sum = d + e + f
    return sum

default_parameter = defa_param(12 , 13)
print(default_parameter)

cities = ["sambajinagar", "nashik","delhi","kolkata","mumbai"]

heros_anime = ["naruto","luffy","Tanjiro","Itachi","Sakura",]

def cities_print(list):
    for iterator in list:
        print(iterator, end=" ")

cities = cities_print(cities)

print(cities)

def heros_print(list):
    for hero in list:
        print(hero , end=" ,")


hero_list = heros_print(heros_anime)
print(hero_list)