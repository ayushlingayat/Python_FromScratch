# *args ==> *args means arbitary positional arguments
# joo multiple arguments lee leta positional arguments okk ek star laga liya toh

def add(*args,name):
    # c = 0
    # print(args)
    # for i in args:
    #     c+= i
    # print(f"The sum of c for multiple callings are {c}")
    print(args)
    print(name)

# add(1,2)
add(1,2,name = "Ayu")
# add(1,3,5,7,9)
# add(2,4,6,8,10)


def adding(a,*adding):
    print(a)
    print(adding)
    c = 0
    for i in adding:
        c+= i
    print(c)



adding(1,2,4,5)
# adding(3,4,5)
# adding(6,7,2)


#arbitary keyword arguments
# kwargs also called as arbitary keyword arguments

def info_keyword(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    for i in args:
        print(i ,end = ' ')
    print()



info_keyword(1,2,3,4,name = "Ayu",age=25,branch = "CSE")
info_keyword(5,6,7,8,name = "Chatur",branch = "CSE")