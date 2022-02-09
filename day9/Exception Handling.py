'''
Error in Python can be of two types i.e. Syntax errors and Exceptions
.Syntax Error: As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of the program.
.Exceptions: Exceptions are raised when the program is syntactically correct, but the code resulted in an error.
This error does not stop the execution of the program, however, it changes the normal flow of the program.


Exception handling?
    .An exception can be defined as an unusual condition in a program resulting in the interruption in the flow of the program.
    .Python provides a way to handle the exception so that the code can be executed without any interruption.
        If we do not handle the exception, the interpreter doesn't execute all the code that exists after the exception.

Why is it important?
    .Whenever an exception occurs, the program stops the execution, and thus the further code is not executed.
    Therefore, an exception is the run-time errors that are unable to handle to Python script. An exception is a
    Python object that represents an error

-->Python provides the number of built-in exceptions, but here we are describing the common standard exceptions.
    A list of common exceptions that can be thrown from a standard Python program is given below.

ZeroDivisionError: Occurs when a number is divided by zero.
NameError: It occurs when a name is not found. It may be local or global.
IndentationError: If incorrect indentation is given.
IOError: It occurs when Input Output operation fails.
EOFError: It occurs when the end of the file is reached, and yet operations are being performed.
'''