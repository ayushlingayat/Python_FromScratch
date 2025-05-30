# Creating a tuple
my_tuple = (10, 20, 30, 20, 40, 50, 20)

# 1. count(x) - Counts the number of times x appears in the tuple
count_20 = my_tuple.count(20)
print(f"Count of 20: {count_20}")

# 2. index(x) - Returns the index of the first occurrence of x
index_30 = my_tuple.index(30)
print(f"Index of 30: {index_30}")

# Tuple is immutable, so you can't add, remove or change elements
# But you can do the following operations:

# 3. Length of tuple
print(f"Length of tuple: {len(my_tuple)}") #{} ashe curly bracket mein likha toh string mein bhi python program chal jata


# 4. Membership test
print(f"Is 40 in tuple? {'Yes' if 40 in my_tuple else 'No'}")

# 5. Iteration
print("Elements in tuple:")
for item in my_tuple:
    print(item, end=' ')
print()

# 6. Tuple concatenation
tuple2 = (60, 70)
new_tuple = my_tuple + tuple2
print(f"Concatenated tuple: {new_tuple}")

# 7. Tuple repetition
repeated = tuple2 * 2
print(f"Repeated tuple: {repeated}")

# 8. Slicing
print(f"Sliced tuple (2 to 5): {my_tuple[2:6]}")