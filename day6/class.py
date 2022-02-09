'''

1.create a class?
    .class definitions begin with a class keyword.
    .The first string inside the class is called docstring and has a brief description of the class.
    Example:'''
class MyNewClass:
    pass


'''2.Attributes and behaviour of class?
    .A class creates a new local namespace where all its attributes are defined. Attributes may be data or functions.
    .There are special attributes that begins with double underscores __
    
    Example:'''
class Person:
    age = 10

    def greet(self):
        print('Hello')
print(Person.age)
print(Person.greet)
print(Person.__doc__)



'''3.write a class using constructor along with its usage?
    .Class functions that begin with double underscore __ are called special functions as they have special meaning.
    .__init__() function gets called whenever a new object of that class is instantiated.
    
    Example:'''
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')

num1 = ComplexNumber(2, 3)

num1.get_data()

num2 = ComplexNumber(5)
num2.attr = 10

print((num2.real, num2.imag, num2.attr))
print(num1.attr)

