'''Functions in python?
        Functions is block of code which only executes when called.
        Parameters when passed through a function returns results.
        Function keeps the code manageable and keeps it organised.
        Code re-usability is achieved using functions.

    -->creating a function'''

#def my_function():
#    print("Tibil solution")
#my_function()

#creating a function with a parameter?

#def my_function(name):
#    print("Hi! my name is " + name)
#my_function('Nikhil')

#using variable in a function?

#def my_function():
    #x = 10
    #print("variable in a function:", x)

#x = 20
#my_function()
#print("value outside function", x)


#absolute value function
'''def absolute_value(digit):
    if digit > 0:
        return digit
    else:
        return -digit
print(absolute_value(-6.9))
print(absolute_value(9))'''

#Built in functions

'''1.abs() function
    The abs() function returns the absolute value of the given number
Example:'''
'''number = -20
absolute_number = abs(number)
print(absolute_number)'''

'''2.any() function
    The any() function returns True if any element of an iterable is True. If not, it returns False.
Example:'''
'''boolean_list = ['True', 'False', 'True']
result = any(boolean_list)
print(result)
'''

'''3.all() function
    The all() function returns True if all elements in the given iterable are true. If not, it returns False.
Example:
'''
'''boolean_list = ['True', 'True', 'True']
result = all(boolean_list)
print(result)
'''

'''4.ascii() method
The ascii() method returns a string containing a printable representation of an object
Example:'''
'''normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')'''

'''5.bin() method 
The bin() method converts and returns the binary equivalent string of a given integer
Example:'''
'''number = 5
print('The binary equivalent of 5 is:', bin(number))'''

'''6.bool() function
The bool() function converts a value to Boolean (True or False) using the standard truth testing procedure.
Example:'''
'''test = []
print(test,'is',bool(test))
test = [0]
print(test,'is',bool(test))
test = 0.0
print(test,'is',bool(test))
test = None
print(test,'is',bool(test))
test = True
print(test,'is',bool(test))
test = 'Easy string'
print(test,'is',bool(test))'''

'''7.callable() method
The callable() method returns True if the object passed appears callable. If not, it returns False.
Example:'''
'''x = 5
print(callable(x))
def testFunction():
  print("Test")
y = testFunction
print(callable(y))
'''

'''8.chr() method 
The chr() method returns a character  from an integer .
Example:'''
'''print(chr(97))
print(chr(65))'''

'''
User defined functions?
    Functions defined by the user to facilitate the code is user defined. 
'''
#user defined function program?

'''def sum(a,b):
    sum = a + b
    return sum
print("The sum of two numbers is:", sum(4, 7))
'''


