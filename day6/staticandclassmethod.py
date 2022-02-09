'''
1 .What is static method?
    The staticmethod() built-in function returns a static method for a given function.

    The syntax of staticmethod() is:
        staticmethod(function)
The staticmethod() method takes a single parameter:function
staticmethod() Return Type:static method of a function.

Example:'''
class Mathematics:

    def addNumbers(x, y):
        return x + y

Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5, 10))


'''2. How to define class method?
    Class method works with the class since its parameter is always the class itself.
    The classmethod() method returns a class method for the given function.

    The syntax of classmethod() method is:
        classmethod(function)

    classmethod() Parameters
    classmethod() method takes a single parameter:Function
    classmethod() Return Value:class method of a function.

    Example:'''
class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

Person.printAge = classmethod(Person.printAge)

Person.printAge()




