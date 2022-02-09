'''
Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.

use of pandas:
Pandas allows us to analyze big data and make conclusions based on statistical theories.
Pandas can clean messy data sets, and make them readable and relevant.
Relevant data is very important in data science.

To check pandas' version
import pandas as pd
print(pd.__version__)

Example:
'''
'''import pandas as pd
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
'''
'''Panda series
A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type.

Example:
'''
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

'''creating labels as series 
With the index argument, you can name your own labels.

Example:
'''
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)
# print(myvar["y"])

'''creating labels as series 
Key/value pair like a dictionary,can also be used to create a panda series
Example:
'''
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
# myvar = pd.Series(calories, index=["day1", "day2"])

print(myvar)
