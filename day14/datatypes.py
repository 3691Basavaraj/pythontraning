'''
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - void
'''
# Example:to check the data type of the array.
import numpy as np

arr = np.array([1, 9.0, 3, 4])
print('The data type is :::',arr.dtype)

print('prints the assigned data type to the array:')
arr1 = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

print('Changing data types of existing array')
arr2 = np.array([1, 2.1, 3.1])
newarr2 = arr2.astype('i')
print('float to int conversion::',newarr2)
print('data type of the above coversion:::',newarr2.dtype)
