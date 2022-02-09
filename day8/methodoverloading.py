'''Method overloading?
    python does not support method overloading by default
    The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method.

Example:'''
class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None, b=None, c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a+b
            return s
s1 = student(3,8)

print(s1.sum(1,2,3))


