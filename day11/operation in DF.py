'''
column selection, addition, and deletion

Selection
Multiple rows can be selected using ‘ : ’ operator.
Example:'''
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df[2:4])


'''Addition of Rows
Add new rows to a DataFrame using the append function. This function will append the rows at the end.
Example:
'''
import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print (df)


'''
Deletion of Rows
Use index label to delete or drop rows from a DataFrame. If label is duplicated, then multiple rows will be dropped.

Example
'''
import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)

# Drop rows with label 0
df = df.drop(0)

print (df)