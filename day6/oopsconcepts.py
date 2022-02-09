'''OOPS concept?
    python supports different programming approaches.
    approaches to solve a programming problem by creating objects is known as Object-Oriented Programming.
    The concept of OOP in Python focuses on creating reusable code(DRY)

1.class
    A class is a blueprint for the object.

    The example for class:
        class car:
            pass
2.object
    An object is an instantiation of a class. When class is defined, only the description
    for the object is defined.
    no memory or storage is allocated.
    An object has two characteristics:
    .attributes
    .behavior

    The example for object :
        obj = Dog()'''

'''3.Inheritance
        .Inheritance is the capability of one class to derive or inherit the properties from another class. 
        .The class that derives properties is called the derived class or base class and the class from which 
        the properties are being derived is called the base class or parent class. 
        .It provides the reusability of a code. We don’t have to write the same code again and again
        .It is transitive in nature, which means that if class B inherits from another class A, 
        then all the subclasses of B would automatically inherit from class A.
        
        Example:'''
class Person(object):

    def __init__(self, name, idnumber):

        self.name = name

        self.idnumber = idnumber



    def display(self):

        print(self.name)

        print(self.idnumber)



    def details(self):

        print("My name is {}".format(self.name))

        print("IdNumber: {}".format(self.idnumber))

class Employee(Person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary

        self.post = post

        Person.__init__(self, name, idnumber)

    def details(self):

        print("My name is {}".format(self.name))

        print("IdNumber: {}".format(self.idnumber))

        print("Post: {}".format(self.post))

a = Employee('Rahul', 886012, 200000, "Intern")

a.display()
a.details()

'''4.polymorphism
    Polymorphism simply means having many forms.
    if we want to determine if a particular object has those specific features.
    
    #example:'''
class Bird:

    def intro(self):
            print("There are many types of birds.")

    def flight(self):
            print("Most of the birds can fly but some cannot.")

class sparrow(Bird):

    def flight(self):
            print("Sparrows can fly.")
class ostrich(Bird):

    def flight(self):

        print("Ostriches cannot fly.")

obj_bird = Bird()

obj_spr = sparrow()

obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


'''
5.Encapsulation
    .Encapsulation describes the idea of wrapping data and the methods that work on data within one unit.
    .It puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
    .A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

    Example:'''
class Base: 

    def __init__(self): 

        self.a = "GeeksforGeeks"

        self.__c = "GeeksforGeeks"

class Derived(Base): 

    def __init__(self): 


        Base.__init__(self) 

        print("Calling private member of base class: ") 

        print(self.__c) 

obj1 = Base() 

print(obj1.a) 

'''
6.Abstraction
    .Abstraction is used to hide the internal functionality of the function from the users.
    .The users only interact with the basic implementation of the function, but inner working is hidden. 
    .An abstraction is used to hide the irrelevant data/class in order to reduce the complexity. 
    .It also enhances the application efficiency.
    
    Abstract class
        .A class that consists of one or more abstract method is called the abstract class. 
        .Abstract methods do not contain their implementation. 
        .Abstract class can be inherited by the subclass and abstract method gets its definition in the subclass.
        
        #Example:
        '''
from abc import ABC, abstractmethod
class Car(ABC):
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")
class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")
class Duster(Car):
     def mileage(self):
          print("The mileage is 24kmph ")

class Renault(Car):
    def mileage(self):
            print("The mileage is 27kmph ")

# Driver code
t= Tesla ()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()
