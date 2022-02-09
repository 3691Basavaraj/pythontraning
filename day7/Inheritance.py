'''Inheritance?

    .Inheritance provides code re-usability to the program because we can use an existing class to
    create a new class instead of creating it from scratch.
    .In inheritance, the child class acquires the properties and can access all the data members and
    functions defined in the parent class.
    .A child class can also provide its specific implementation to the functions of the parent class.

    Example:'''
class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def bark(self):
        print("dog barking")
d = Dog()
d.bark()
d.speak()

