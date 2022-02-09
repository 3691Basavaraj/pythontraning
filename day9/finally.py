'''-->
    .Python provides a keyword finally, which is always executed after the try and except blocks.
    .The final block always executes after normal termination of try block or after try block terminates due to some exception.

Syntax:

try:
    # Some Code
except:
    # Executed if error in the
    # try block
else:
    # execute if no exception
finally:
    # Some code .....(always executed)'''

#Example:

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
try:
    print(a/b)
except Exception:   #executes only when try has a errror.
    print("division not possible")
else:
    print("No exception found!")   #executes only when no exception is found.

finally:
    print("print this in either of the cases above") #executes np matter what the condition is!