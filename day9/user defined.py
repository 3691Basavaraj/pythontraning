'''User defined?
    .In Python, users can define custom exceptions by creating a new class. This exception class has to be derived, either directly or indirectly,
    from the built-in Exception class. Most of the built-in exceptions are also derived from this class.

    -->Deriving Error from Super Class Exception

    .Superclass Exceptions are created when a module needs to handle several distinct errors. One of the common ways of doing
    this is to create a base class for exceptions defined by that module. Further, various subclasses are defined to create
    specific exception classes for different error conditions.

    Example:'''
'''class Error(Exception):

    # Error is derived class for Exception, but
    # Base class for exceptions in this module
    pass

class TransitionError(Error):

    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = nex

        # Error message thrown is saved in msg
        self.msg = msg
try:
    raise(TransitionError(2,3*2,"Not Allowed"))

# Value of Exception is stored in error
except TransitionError as error:
    print('Exception occured: ',error.msg)'''

'''-->Exceptions as a base class?
    .A runtime error is a class that is a standard exception that is raised when a generated error does not fall into any category. 
    This program illustrates how to use runtime error as base class and network error as derived class. In a similar way,
    an exception can be derived from the standard exceptions of Python.
    
Example:'''
class carservice(Exception):
    pass


class charges(carservice):
    pass


class services(carservice):
    pass


service_center = 'open'
try:
    if service_center == 'open':
        raise services
    else:
        print('Please visit Tomorrow:')

except charges:
    print('The charges are:')
except services:
    print('The services offered are.....:')

finally:
    print("Thank you for Visiting")

