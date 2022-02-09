'''
1.instance variable?
    Variables that are owned by the class instances are known as instance variables
    every instance or object of a class, the instance variables are unlike.
    instance variables, owned by the class objects, enable the developers to store different values in each instance assigned to those variables.
2.instance method?
    instance methods: Used to access or modify the object state. If we use instance variables inside a method,
    such methods are called instance methods. It must have a self parameter to refer to the current object.

3.ways to declare an instance variable?
    Instance variables are declared inside a method using the self keyword. We  can use a constructor
    to define and initialize the instance variables.
Example:'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Jessa", 20)

print('Object 1')
print('Name:', s1.name)
print('Age:', s1.age)

s2= Student("Kelly", 10)

print('Object 2')
print('Name:', s2.name)
print('Age:', s2.age)



#4.example of a class with instance variables in different locations?
#Example:
import types

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('Name:', self.name, 'Age:', self.age)

def welcome(self):
    print("Hello", self.name, "Welcome to Class IX")

s1 = Student("Jessa", 15)

s1.welcome = types.MethodType(welcome, s1)
s1.show()

s1.welcome()


'''5.How to initialize instance variables with different values?
    syntax to add the new instance variable to the object:
            object_reference.variable_name = value.
            Example:'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stud = Student("Jessa", 20)

print('Before')
print('Name:', stud.name, 'Age:', stud.age)
stud.marks = 75
print('After')
print('Name:', stud.name, 'Age:', stud.age, 'Marks:', stud.marks)


'''6.How to access an instance variable outside the class?
    We can access instance variables of one class from another class using object reference.
    This is useful when we want to access the parent class instance variable from a child class.
    Example:'''
class Vehicle:
    def __init__(self):
        self.engine = '1500cc'

class Car(Vehicle):
    def __init__(self, max_speed):
        super().__init__()
        self.max_speed = max_speed

    def display(self):
        print("Engine:", self.engine)
        print("Max Speed:", self.max_speed)

car = Car(240)
car.display()


'''7.How to access instance variables inside an instance method ?
There are two ways to access the instance variable of class:
    Within the class in instance method by using the object reference (self)
        Example:'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('Name:', stud.name, 'Age:', stud.age)

stud = Student("Jessa", 20)

stud.show()

'''Using getattr() method
        Pass the object reference and instance variable name to the getattr() method to get the value of
        an instance variable.

        Example:'''
class Student:

    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

stud = Student("Jessa", 20)

print('Name:', getattr(stud, 'name'))
print('Age:', getattr(stud, 'age'))


