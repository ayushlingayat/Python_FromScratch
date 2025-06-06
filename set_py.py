#set is the collection of unorder_items
#Each element in the set must be unique and immutable

#order matter nhi karta hee idar
collection_set = {1,2,3,4,"hello","hello",2}
#duplicate value automatically ignore okk


#set mutable hee lekin uske elements immutable hee okk

print(collection_set)
print(type(collection_set))

empty_dictionary = {}

#syntax of empty dictionary
print(empty_dictionary)

#creating empty set
collection = set()

print(type(collection))

#set methods
# .add method mein hum tuple pass krr sakhte hee not list and dictioanry
#because vooh immutable hote hee

set_play = set()

set_play.add(1)
set_play.add(2)
set_play.add(3)
set_play.add(4)
set_play.add((1,2,3,4,5,6,7,8,9))
set_play.add("ayush")

set_play.remove(1)
set_play.remove(2)

set_play.clear()

print(len(set_play))


#random value mein elements pop hote means khuch bhi pop hoga ismein seeh

set_pop = {"Ayush" , "Lingayat" , "Learning" , "Python"}

pop_el = set_pop.pop()

print(pop_el)

# set important methods union and intersection methods of set

# set returns us a new set here union and intersection are just like maths we have done in our past

set1 = {1,2,3,4,5,6,7,8,9}

set2 ={1,2,3,10,20,30,40,50}

union_sets = set1.union(set2)
print(union_sets)

union_intersection = set1.intersection(set2)
print(union_intersection)


