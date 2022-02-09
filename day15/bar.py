'''
With Pyplot, you can use the bar() function to draw bar graphs:
'''
# Example:
import matplotlib.pyplot as plt
import numpy as np

'''x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
'''
# Example::

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
'''print('1.prints horizontal bars--')
plt.barh(x, y)'''
'''print('2.prints bars with green color--')
plt.bar(x, y, color = 'green')'''
print('3.prints bars with specified bar width::--')
plt.barh(x, y, color='#F08080')
'''print('3.prints bars with specified bar height::--')
plt.barh(x, y, height=0.1)'''
plt.show()
