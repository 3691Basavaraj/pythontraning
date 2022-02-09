'''1.An iterator is an object that contains a countable number of values.
2.An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
3.In Python, an iterator is an object which implements the iterator protocol,
which consist of the methods __iter__() and __next__().

Example:
'''
mytuple = ("apple", "banana", "cherry")
it = iter(mytuple)

print(next(it))
print(next(it))
print(it.__next__())

# Example:  Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

'''1.To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object
2.The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
3.The __next__() method also allows you to do operations, and must return the next item in the sequence.

Example:'''


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# Example: To prevent the iteration to go on forever, we can use the StopIteration statement.

class Topten:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            value = self.num
            self.num += 1

            return value


val = Topten()
for x in val:
    print(x)
