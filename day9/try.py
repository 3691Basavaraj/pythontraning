'''
1.First, the try clause is executed i.e. the code between try and except clause.
2.If there is no exception, then only the try clause will run, except the clause is finished.
3.If any exception occurs, the try clause will be skipped and except clause will run.
4.If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements.
5.If the exception is left unhandled, then the execution stops.
6.A try statement can have more than one except clause


Syntax:

try:
    # Some Code
except:
    # Executed if error in the
    # try block

Example:'''

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
try:
    print(a/b)
except ZeroDivisionError:   #executes only when try has a errror.
    print("division not possible")


