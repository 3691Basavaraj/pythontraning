'''
The Pandas offers .loc[] and .iloc[] methods for data slicing.
These two methods belong to the index selection method that is used to set an identifier for each row of the data set.


#loc[] method
The .loc[] method is used to retrieve the group of rows and columns by labels or a boolean array present in the DataFrame.
It takes only index labels, and if it exists in the caller DataFrame, it returns the rows, columns, or DataFrame.
It is a label-based method but may be used with the boolean array.

Example:
'''
import pandas as pd

df = pd.DataFrame([[2, 3], [5, 6], [8, 9]],
                      index=['cobra', 'viper', 'sidewinder'],
                      columns=['max_speed', 'shield'])
print(df)
print(df.loc['viper'])
print(df.loc[['viper', 'sidewinder']])

'''iloc[] method
The .iloc[] method is used when the index label of the DataFrame is other than numeric series of 0,1,2,....,n, or in
the case when the user does not know the index label.
'''
# Example:

'''import pandas as pd

mydict = [{'p': 2, 'q': 3, 'r': 4, 's': 5},
          {'p': 20, 'q': 30, 'r': 40, 's': 50},
          {'p': 200, 'q': 300, 'r': 400, 's': 500}]
df = pd.DataFrame(mydict)
print(df)
print(df.iloc[[0]])
type(df.iloc[[0]])
'''
