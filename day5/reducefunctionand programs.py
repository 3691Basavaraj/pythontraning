'''Reduce function?
    The reduce  function is used to apply a particular function passed in its argument to all of the
    list elements mentioned in the sequence passed along.
    The reduce function is defined in “functools” module.

    Sytax::

Working :

1.At first step, first two elements of sequence are picked and the result is obtained.
2.Next step is to apply the same function to the previously attained result and the number just succeeding the
second element and the result is again stored.
3.This process continues till no more elements are left in the container.
4.The final returned result is returned and printed on console.'''

#Example:

#using 3 parameters.
# Python program to  illustrate sum of two numbers.
'''def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
tup = (2, 1, 0, 2, 2, 0, 0, 2)
print(reduce(lambda x, y: x + y, tup, 6))
'''
#using operator

'''import functools
import operator
lis = [1, 3, 5, 6, 2, ]
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))
'''

#using accumulate function.
'''import itertools
import functools
lis = [1, 3, 4, 10, 4]
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x + y)))'''

#program to add all the number from a list using reduce function.

'''import functools
lis = [1, 3, 5, 6, 2, ]
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))
'''
#program to add all the number from a list without using reduce function.

'''list1 = [11, 5, 17, 18, 23]
total = 0
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("Sum of all elements in given list: ", total)'''