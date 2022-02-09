'''
Filtering Arrays
Getting some elements out of an existing array and creating a new array out of them is called filtering.
In NumPy, you filter an array using a boolean index list.
'''
# Example:
import numpy as np

'''arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)'''
'''
Searching Arrays
You can search an array for a certain value, and return the indexes that get a match.
To search an array, use the where() method.'''
# Example:
'''print('prints the indices of the element specified(4)')
arr1 = np.array([1, 2, 3, 4, 5, 4])
x = np.where(arr1 == 4)
print(x)'''

print('returns the given value at a specified index')
arr2 = np.array([6, 7, 8, 9])
l2 = [1,2,8,4,5]
arr2.append(l2)



#x = np.searchsorted(arr2, num)
print(arr2)

'''
Splitting NumPy Arrays
Splitting is reverse operation of Joining.
Joining merges multiple arrays into one and Splitting breaks one array into multiple.
 use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

'''
# Example:
'''print('splitting array into 4 parts::')
arr = np.array([1, 2, 3, 4, 5, 6,7])
newarr = np.array_split(arr, 4)
print(newarr)
print('accessing the split arrays using index value')
print(newarr[0])
print(newarr[1])
print(newarr[2])
print(newarr[3])'''

'''Sorting Arrays
Sorting means putting elements in an ordered sequence.
Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
The NumPy ndarray object has a function called sort(), that will sort a specified array.'''
# Example:
'''print('sorted array is ::')
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))


print('Sorting 2-D array::')
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))'''
