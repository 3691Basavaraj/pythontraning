'''
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.


Use of Numpy
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
This behavior is called locality of reference in computer science.
This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.
'''
import numpy as np

'''arr = np.array([[1, 2, 3, 4, 5]])
# print(type(arr))
ar = arr[0,2]#prints the specified index of the array
arr[0,2] = 55 #returns the updated array
print((arr))
print(arr.shape)  #retuns the matrix count of the array
print(arr.size) #returns the size of the array'''

'''NumPy Array Copy vs View
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
'''
#Example:
print("Numpy copy")
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)


print('Numpy view')
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

print('changes to view ')
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)