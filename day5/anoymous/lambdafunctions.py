'''Lambda function?
    A lambda function is a small anonymous function that is defined without a name.
    A lambda function can take any number of arguments, but can only have one expression.

    Syntax:
    lambda arguments : expression
'''

#Example:
'''x = lambda a, b, c : a + b * c
print(x(5, 6, 2))'''


# Program to filter out only the even items from a list

'''my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)'''