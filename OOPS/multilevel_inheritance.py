# Base class
class Grandparent:
    def show_grandparent(self):
        print("I am the grandparent")

# Intermediate class
class Parent(Grandparent):
    def show_parent(self):
        print("I am the parent")

# Derived class
class Child(Parent):
    def show_child(self):
        print("I am the child")

# Creating object
c = Child()
c.show_grandparent()
c.show_parent()
c.show_child()
