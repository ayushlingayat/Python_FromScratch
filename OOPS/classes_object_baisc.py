#
# #class is a blueprint to create a object
# class Student:
#     name = "Ayush"
#     age = 24
#
# # creating the instance of the means object here
# s1 = Student()
# print(s1.name)
# print(s1.age)


# ek aur example lee lete hee jidar hum factory bana rahe hee
# aur car produce karr rahe hee

# so car kee properties kya honge in blue print like
# color, wheels , engine, nitro

# class Car:
#     colour = "Red"
#     wheels = 4
#     engine = "Double boosted engine"
#     nitro = "Best quality"
#
#
# car1 = Car()
# print(car1.colour)
# print(car1.wheels)

# I can create multiple object here okk just remember that

# car2 = Car()
# print(car2.engine)
# print(car2.nitro)


#constructor in python

# __init__ Function in python is a contructor okk
# yeeh function object creation kee time prr naa invoke hota hee
# constructor humesha ek self parameter leta hee okk
# jab bhi koi object create hora hee ushi kaa reference matlab self hota hee okk
#remember self humesha first parameter hota hee okk
#self parameter kee baad hum dusre parameter bhi dee sakhte hee jese for example
# class Student:
#     #now I will initialize the constructor over here
#     def __init__(self,fullname):
#         print("This is automatically invoked when the object is created")
#         self.name = fullname
#         #self.name matlab ek name variable banaya humne idar okk aur usko naa object creation kee time joo name denge vooh assign kiya samje
#
#
# student_obj = Student("Ravi")
# print(student_obj.name)


class Car:
    colour = "Blue"
    model = "BMW"
    wheels = 4
    nitro = "Full Speed"
    def __init__(self,colour,model,wheels,nitro):
        print("My blueprint for cars")
        self.colour = colour
        self.model = model
        self.wheels = wheels
        self.nitro = nitro


car1 = Car("Blue","BMW","4","Excellent Nitro")
print(car1.colour)
print(car1.model)
print(car1.wheels)
print(car1.nitro)

print("-" * 50)

car2 = Car("Red","Toyota","4","Boosted Nitro")
print(car2.colour)
print(car2.model)
print(car2.wheels)
print(car2.nitro)

print("-" * 50)

car3 =Car("Black","Nano Car","4","No Nitro")
print(car3.colour)
print(car3.model)
print(car3.wheels)
print(car3.nitro)


print("<->" * 50)

class Students:
    college_name = "XYZ College" #class attribute
    #yeeh fix rahte for all object remember that
    #yeeh common rahega har object kee liye
    # because naa idar naa self see attributes(varibles)
    # nhi create kare humne

    # Defining class method here
    def welcome(self):
        print("Welcome student how are you ?" , self.name)


    def getMarks(self):
        return self.marks

    #default constructor
    def __init__(self):
        pass

    #parameterised constructor
    def __init__(self,name,marks,subject):
        print("created another object instance")
        self.name = name #instance attribute
        self.marks = marks #instance attribute
        self.subject = subject #instance attribute


s1 = Students("Ayush",99,"Maths")
print(s1.name,s1.marks,s1.subject)
print(Students.college_name) #this is also valid
print(s1.college_name)

s2= Students("Piyush",100,"History")
print(s2.college_name)
s2.welcome()
s1.welcome()
print(s1.getMarks())
print(s2.getMarks())

# object arribute presidence is higher then object attribute also called instance attribute

print("👾" * 50)

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum = sum + val
        print("Hii",self.name,"you average of marks is", sum/3)

    @staticmethod
    #@staticmethod dala naa self likhne kii jarurat nhi rehti okk understand that
    # jaha self kaa use nhi khuch vaha @staticmethod use karna okk
    def hello(): #decorator
        print("Hello I am Ayush How are you people")

stud1 = Student("Ayush",[86,68,99])
stud1.get_avg()

stud1.name = "Spiderman"
stud1.get_avg()
stud1.hello()