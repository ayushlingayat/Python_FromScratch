# String Methods Demo in Python

# Sample string
text = "hello world, welcome to the world of Python."

print("Original Text:", text)

# 1. endswith(suffix)
# Checks if the string ends with the given suffix
print("\n1. endswith('Python.') →", text.endswith('Python.'))  # True
print("   endswith('world') →", text.endswith('world'))        # False

# 2. capitalize()
# Capitalizes the first character of the string and lowercases the rest
capitalized_text = text.capitalize()
print("\n2. capitalize() →", capitalized_text)
# Output: 'Hello world, welcome to the world of python.'

# 3. replace(old, new)
# Replaces all occurrences of 'old' substring with 'new'
replaced_text = text.replace("world", "universe")
print("\n3. replace('world', 'universe') →", replaced_text)
# Output: 'hello universe, welcome to the universe of Python.'

# 4. find(sub)
# Returns the lowest index where the substring is found, else -1
index_python = text.find("Python")
index_hello = text.find("hello")
index_java = text.find("Java")  # Not found
print("\n4. find('Python') →", index_python)   # Position of 'Python'
print("   find('hello') →", index_hello)       # 0
print("   find('Java') →", index_java)         # -1

# 5. count(sub)
# Counts how many times a substring appears in the string
count_world = text.count("world")
count_o = text.count("o")
print("\n5. count('world') →", count_world)    # 2
print("   count('o') →", count_o)              # 5
