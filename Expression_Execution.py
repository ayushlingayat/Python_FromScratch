A = 2
B = 3
Txt = "@"

print(A*Txt*B)

# Jab bhi koi bhi string numeric value seeh
# multiple hoti hee vooh utni baar repeat hogi
# in that case always remember

# 1 - First Rule of Expression Execution hee yeeh yaad rakhna

str_A = "2"
str_B ="@"
c = 3

print((str_A + str_B) * c)

# String + String = Concatenation

#2 - Numeric values can operate with all arithematic operators

print(A + B * c)
# Bodmas Rule apply hua idar okk

# 3 - Arithematic Express with Integer and Float will always result in float
A_,B_ = 4 , 5.0
C_ = A_ * B_
print(C_)
#Answer always comes in float

#Result of division operator with two integer is always float
div_a =1
div_b =2
div_c =div_a /div_b
print(div_c)
#always float answer will come

# 4- int division with float and Int will give will give int displayed as float

d , e = 1.5 , 3
f = d//e
print(f , d/e)
#orginal answer 0.5 ayega but yeh round off karta hee
# samllest number tak isliye
# answer mein float ayega 0.0

# d//e is same as floor function okk
# floor(d/e)

# 5 - Remainder is negative when denominator is negative
# n = +ve and d = -ve then only negative answer ayega

z, u = 5 ,-2
p = z%u
print(p)

#Comments

# => Denotes single line comment as well as Multi-line too

"""Hii bhai ayush bol raha
yeeh multi line comment jesa act karra idar"""

