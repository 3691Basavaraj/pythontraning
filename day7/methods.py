'''
1 .What is static method?
    The staticmethod() built-in function returns a static method for a given function.

    The syntax of staticmethod() is:
        staticmethod(function)
The staticmethod() method takes a single parameter:function
staticmethod() Return Type:static method of a function.

Example:'''
class Students:
    school = 'GIT'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def average(self):
        return (self.m1 + self.m2 + self.m3/3)

    @classmethod
    def info(cls):
        return cls.school
s1 = Students(3,4,7)
s2 = Students(6,9,6)

print(s1.average())
print(Students.info())

'''2. How to define class method?
    Class method works with the class since its parameter is always the class itself.
    The classmethod() method returns a class method for the given function.

    The syntax of classmethod() method is:
        classmethod(function)

    classmethod() Parameters
    classmethod() method takes a single parameter:Function
    classmethod() Return Value:class method of a function.

    Example:'''
class Students:
    school = 'VTU'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def average(self):
        return (self.m1 + self.m2 + self.m3/3)

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is static method")
s1 = Students(3,4,7)
s2 = Students(6,9,6)

print(s2.average())
print(Students.getschool())

