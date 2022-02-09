'''
Access Array Elements
Array indexing is the same as accessing an array element.
 can access an array element by referring to its index number.
The indexes in NumPy arrays start with 0,
'''
# Example:Accessing 1D array
import numpy as np

'''arr = np.array([1, 2, 3, 4])
print('Accessed element on the Zero index is:',arr[0])
print('Addition of 3 and 4 is :', arr[2] + arr[3])'''

# EXample:Accessing 2-D array
'''arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
print('1st element in 2nd row:', arr[1,0])
print('Negetive indexing output: ', arr[1, -1])
'''

# Example:accessing 3-D array
'''arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('Accessing element in the 3-D array is...\n',arr[1, 1, -1])'''

'''Slicing arrays
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].'''
# Example:
'''arr = np.array([1, 2, 3, 4, 5, 6, 7])
print('Slicing Elements from index 1 to 4 are:', arr[1:5])
print('Slicing Elements from index 4 till the end are:', arr[1:])
print('Slicing Elements from index 0 till 4 are:', arr[:4])
print('Negetive slicing:', arr[-3:-1])
print('Step slicing:', arr[1:5:2])
print('printing by skipping two elements in whole array:', arr[::3])'''


#Example:slicing for 2-D array
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Returns index 2 form both the elements:::', arr1[0:2, 2])
print(arr1[0:2, 1:4])