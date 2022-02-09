'''
Raise exception?
    An exception can be raised to throw an error if certain conditions occur.
'''
#Example:



x = int(input("Enter the first number"))
if x>6:
    raise Exception('x should not exceed 6.The value of x is:', x)