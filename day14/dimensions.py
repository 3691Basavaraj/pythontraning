'''
1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.'''
# Example:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print('1-D array is :::',arr)

'''
2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.
'''
# Example:
arr1 = np.array([[1, 2, 3], [4, 5, 6]])

print('2-D array is ::',arr1)

'''3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.'''
# Example:
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print('3-D array is::',arr2)

print('the dimension the above array is', arr.ndim)
