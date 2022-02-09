'''
The plot() function is used to draw points (markers) in a diagram.
By default, the plot() function draws a line from point to point.
The function takes parameters for specifying points in the diagram.
Parameter 1 is an array containing the points on the x-axis.
Parameter 2 is an array containing the points on the y-axis.
'''
#Example::
import matplotlib.pyplot as plt
import numpy as np
print('plotting using x and y axis:')
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()


'''Plotting Without Line
To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.'''
#Example::
'''print('plotting without lines')
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()'''

'''Multiple Points
You can plot as many points as you like, just make sure you have the same number of points in both axis.'''
#Example:
'''print('plotting using multiple points')
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
'''
'''
Default X-Points
If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.

So, if we take the same example as above, and leave out the x-points, the diagram will look like this:'''

#Example
'''print('Plotting without x-points:')


ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()'''

DONE