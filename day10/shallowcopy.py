'''
1.copy module of Python for shallow and deep copy operations.
2.A shallow copy creates a new object which stores the reference of the original elements.
3.A shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects

Syntax:
import copy
copy.copy(x)

Example:
'''
import copy

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = copy.copy(list1)

# list1[0][2] = 'b'

print(list1)
print(list2)
