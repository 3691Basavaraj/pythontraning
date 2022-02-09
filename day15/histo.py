'''
A histogram is a graph showing frequency distributions.
It is a graph showing the number of observations within each given interval.
In Matplotlib, we use the hist() function to create histograms.
The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.
'''
#Example::
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(110, 10)
y = np.random.normal(90, 80)

plt.hist(x)
plt.hist(y)
plt.show()