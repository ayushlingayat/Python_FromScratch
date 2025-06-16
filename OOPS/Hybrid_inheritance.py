# Base class
class A:
    def method_A(self):
        print("Method from class A")

# Derived from A
class B(A):
    def method_B(self):
        print("Method from class B")

# Another base class
class C:
    def method_C(self):
        print("Method from class C")

# Derived from both B and C (Multiple + Multilevel)
class D(B, C):
    def method_D(self):
        print("Method from class D")

# Creating object
obj = D()
obj.method_A()
obj.method_B()
obj.method_C()
obj.method_D()
