# Length function in string
str1 = "Ayush"
str2 ="Lingayat"
str_1_len = len(str1)
str_2_len = len(str2)
print(str_1_len)
print(str_2_len)

final_str = str1 + " " + str2
#idar naa empty space bhi count hua in length
#function okk humesha yaad rakhna
print(len(final_str))

# string kee andar changes nhi
# krr sakhte hee apen okk

# first_char = str1[0] = "@"
# print(first_char)
# not valid program will not run
# yeeh valid nhi hee because string mein changes nhi krr sakhte hee apen

#we can access the character of the string but cannot modify them
s = "PythonString"

print("Original String:", s)

# Basic slicing
print("\n1. s[0:6]      →", s[0:6])        # 'Python'
print("2. s[6:]        →", s[6:])         # 'String'
print("3. s[:6]        →", s[:6])         # 'Python'
print("4. s[:]         →", s[:])          # 'PythonString'

# Negative indexing
print("\n5. s[-6:]       →", s[-6:])        # 'String'
print("6. s[:-6]       →", s[:-6])        # 'Python'