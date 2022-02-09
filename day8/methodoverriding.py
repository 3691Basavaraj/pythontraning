'''
method overriding?
    .Method overriding is an ability of any object-oriented programming language that allows a subclass or child class
    to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes
    .When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type)
    as a method in its super-class, then the method in the subclass is said to override the method in the super-class.
Example:'''


class Parent():

    def __init__(self):
        self.value = "Inside Parent"

    def show(self):
        print(self.value)

class Child(Parent):

    def __init__(self):
        self.value = "Inside Child"

    def show(self):
        print(self.value)

obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()

#Method overriding with multiple and multilevel inheritance
#Example using Multiple inheritance
class Parent1():

    def show(self):
        print("Inside Parent1")

class Parent2():
    def display(self):
        print("Inside Parent2")

class Child(Parent1, Parent2):

    def show(self):
        print("Inside Child")

obj = Child()

obj.show()
obj.display()

#Example using Multiple inheritance
class Parent():

    def display(self):
        print("Inside Parent")

class Child(Parent):

    def show(self):
        print("Inside Child")

class GrandChild(Child):

    def show(self):
        print("Inside GrandChild")

g = GrandChild()
g.show()
g.display()