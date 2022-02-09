'''
Create a DataFrame.
Example:
'''
import pandas as pd
data1 = [1,2,3,4,5]  #using list
data2 = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}   #using dictionaries
data3 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]   #using list of dictionaries

data4 = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]  #usisng list of dictionaries

data5 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(data1)
df = pd.DataFrame(data2)
df = pd.DataFrame(data3)
df = pd.DataFrame(data5)
#df = pd.DataFrame(data4, index=['first', 'second'])
print (df)


'''
data of DataFrames 
Accessing data from series with Position:

.Value
.Columns
.Rows

Example:
.Columns
'''
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df ['one'])  #prints colum one




