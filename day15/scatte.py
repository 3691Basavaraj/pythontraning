'''With Pyplot, you can use the scatter() function to draw a scatter plot. The scatter() function plots one dot for
each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the
y-axis:
'''
# Example:
import matplotlib.pyplot as plt
import numpy as np

'''print('plots the scattered dots according to specified value')
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

plt.scatter(x, y, color='black')
plt.show()'''

# Using colormap
# ::colormap is created by including the plt.colorbar() statement:
# Size::You can change the size of the dots with the s argument.
# alpha::Adjust the transparency of the dots with the alpha argument.



x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])
plt.scatter(x, y, c=colors, cmap='BuGn', s=sizes, alpha=0.9)

plt.colorbar()
plt.show()
