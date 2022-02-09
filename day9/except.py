'''
--->
A try statement can have more than one except clause, to specify handlers for different exceptions
Synatx:
try:
    # statement(s)
except IndexError:
    # statement(s)
except ValueError:
    # statement(s)
'''
# Example:

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

try:
    c = a/b
    print(c)
except ZeroDivisionError:  # executes only when try has an error.
    print("division not possible")


try:
    mylist = [1, 2, 3, 4, 5]
    print(mylist[1])
except IndexError:
    print('Index not found')
