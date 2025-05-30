# Arrays kaa hee equivalent humare pass naa list hota hee in python

# In Python, a list can contain elements of different data types
# all mixed together.
# This is one of the flexible features of Python lists.

# List Operations and Methods in Python

# Creating a list
fruits = ["apple", "banana", "cherry", "banana"]
print("Original list:", fruits)

# 1. Accessing elements using index
print("\n1. Access by index → fruits[1]:", fruits[1])  # banana

# 2. Negative indexing
print("2. Negative index → fruits[-1]:", fruits[-1])  # banana

# 3. Slicing
print("3. Slicing → fruits[1:3]:", fruits[1:3])  # ['banana', 'cherry']


#Methods start
# 4. append() – Add single item to the end
fruits.append("orange")
print("\n4. append('orange') →", fruits)

# 5. insert(index, value) – Insert at specific index
fruits.insert(1, "kiwi")
print("5. insert(1, 'kiwi') →", fruits)

# 6. extend() – Add multiple elements
fruits.extend(["mango", "grape"])
print("6. extend(['mango', 'grape']) →", fruits)

# 7. remove(value) – Remove first occurrence
fruits.remove("banana")
print("\n7. remove('banana') →", fruits)

# 8. pop() – Remove last item (or by index)
popped = fruits.pop()
print("8. pop() →", popped)
print("   List after pop →", fruits)

# 9. index(value) – Get index of first occurrence
print("\n9. index('cherry') →", fruits.index("cherry"))

# 10. count(value) – Count occurrences
print("10. count('banana') →", fruits.count("banana"))

# 11. sort() – Sort in ascending order
numbers = [3, 1, 4, 2, 5]
numbers.sort()
print("\n11. sort() →", numbers)

# 12. reverse() – Reverse the list
numbers.reverse()
print("12. reverse() →", numbers)

# 13. copy() – Shallow copy of list
copy_list = fruits.copy()
print("\n13. copy() →", copy_list)

# 14. clear() – Empty the list
temp = [1, 2, 3]
temp.clear()
print("14. clear() →", temp)

# 15. List Comprehension
squares = [x**2 for x in range(1, 6)]
print("\n15. List Comprehension → Squares:", squares)

# 16. Membership test
print("\n16. 'apple' in fruits →", "apple" in fruits)
print("    'papaya' not in fruits →", "papaya" not in fruits)

# 17. Nested list access
nested = [[1, 2], [3, 4], [5, 6]]
print("\n17. Nested list → nested[1][0]:", nested[1][0])  # 3
