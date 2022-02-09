'''
1.Single Inheritance
    .Single level inheritance is achieved when a derived class inherits the properties of parent class.
Syntax:
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class

  Example:'''
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child(Parent):
    def func2(self):
        print("This function is in child class.")

object = Child()
object.func1()
object.func2()

'''2.Multiple Inheritance
    .When a class can be derived from more than one base class this type of inheritance is called multiple inheritance
    .In multiple inheritance, all the features of the base classes are inherited into the derived class. 
Syntax:
class BaseClass1:
Body of base class
class Baseclass2:
Body of base class2
class DerivedClass(BaseClass1,Base class2)
  Body of derived class'''

'''class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
 
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
 

class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()'''

'''3.Multilevel Inheritance
    .Multi-level inheritance is archived when a derived class inherits another derived class.
    .There is no limit on the number of levels up to which, the multi-level inheritance is archived in python.
Syntax:
class BaseClass:
Body of base class
class Baseclass2(Baseclass):
Body of base class2
class DerivedClass(Base class2)
  Body of derived class
Example:'''

'''class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        Grandfather.__init__(self, grandfathername)

class Son(Father):
    def __init__(self,sonname, fathername, grandfathername):
        self.sonname = sonname

        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)

s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()'''

'''4.Hierarchical Inheritance
    .When more than one derived classes are created from a single base this type of 
    inheritance is called hierarchical inheritance
Syntax:
class BaseClass:
  Body of base class
class DerivedClass1(BaseClass):
  Body of derived class1
class DerivedClass2(BaseClass):
  Body of derived class2

Example:'''
'''class Parent:
      def func1(self):
          print("This function is in parent class.")

class Child1(Parent):
      def func2(self):
          print("This function is in child 1.")

class Child2(Parent):
      def func3(self):
          print("This function is in child 2.")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()'''

'''5.Hybrid Inheritance
    .Inheritance consisting of multiple types of inheritance is called hybrid inheritance.
Example:'''
class School:
    def func1(self):
        print("This function is in school.")

class Student1(School):
    def func2(self):
        print("This function is in student 1. ")

class Student2(School):
    def func3(self):
        print("This function is in student 2.")

class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

object = Student3()
object.func1()
object.func2()