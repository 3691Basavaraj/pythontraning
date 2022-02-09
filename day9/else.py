'''-->
    .You can use the else keyword to define a block of code to be executed if no errors were raised:
    .In python, you can also use the else clause on the try-except block which must be present after all the except clauses.
    The code enters the else block only if the try clause does not raise an exception.

Syntax:

try:
    # Some Code
except:
    # Executed if error in the
    # try block
else:
    # execute if no exception

#Example:'''

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
try:
    print(a/b)
except Exception:   #executes only when try has a errror.
    print("division not possible!")
else:
    print("No exception found!")   #executes only when no exception is found.


