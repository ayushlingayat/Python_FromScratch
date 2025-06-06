#keys mein list aur dictionary use nhi krr sakhte hum log okk humesha yaad rahkna
#there is no order in dictionary and as well as mutable bhi hote hee yeeh cheez okk

# list aur dictionary dono mutable hoti hee
#duplicate key nhi create krr sakhte


dict = {
    "name" : "Ayush Lingayat",
    "age" : 24,
    "marks" : 99.99,
    "subject" : "Python",
    12.99: 9.4
}

print(type(dict))

#printing values using key

print(dict["name"])
print(dict["age"])
print(dict["subject"])
print(dict[12.99])

dict["name"] = "Shradha Didi"
print(dict["name"])

#adding new key-value pair here

dict["surname"] = "Lingayat"

print(dict)

#Empty dictionary

emp_dict = {}
print(emp_dict)
print(type(emp_dict))

#nested dictionary

students ={
    "name" : "Ayush",
    "age" : 24,
    "Education" : "MCA",
    "Subject" : {
        "physics": 99,
        "chemistry" : 74,
        "math": 100
    },
    "Roll_no" : 37
}

print(students["Subject"]["math"])

students["Subject"]["math"] = 50

print(students["Subject"]["math"])

#methods of dictionary

print(list(students.keys()))

print(students.keys())

print(list(students.values()))

print(students.items())
dict_store_list = list(students.items())

print(dict_store_list[0])

print(students.get("name"))

students.update({"city" :"Sambajinagar"})

print(students) #yaha pee update hoga city okk check karr lena





