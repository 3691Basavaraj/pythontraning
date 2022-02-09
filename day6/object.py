'''
1.what is an object?
    .An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class
      with actual values
    .An object consists of :
    State: It is represented by the attributes of an object. It also reflects the properties of an object.
    Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
    Identity: It gives a unique name to an object and enables one object to interact with other objects.

    Example:'''
class Dog:

    attr1 = "mammal"
    attr2 = "dog"

    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()


'''2.ways to create an object?
a.The self
        .Class methods must have an extra first parameter in the method definition. We do not give a value
        for this parameter when we call the method, Python provides it
        .If we have a method that takes no arguments, then we still have to have one argument.
        .When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by
        .Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.
    b.The __init__ method
        .The __init__ method is run as soon as an object of a class is instantiated.
        .The method is useful to do any initialization you want to do with your object.

        Example:'''
class Dog:

    attr1 = "animal"

    def __init__(self, name):

        self.name = name

Rodger = Dog("Rodger")

Tommy = Dog("Tommy")

print("Rodger is a {}".format(Rodger.__class__.attr1))

print("Tommy is also a {}".format(Tommy.__class__.attr1))

print("My name is {}".format(Rodger.name))

print("My name is {}".format(Tommy.name))


