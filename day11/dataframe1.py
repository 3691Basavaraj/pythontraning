'''
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
A DataFrame is the whole table.

Example:
'''
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
#refer to the row index:
#print(df.loc[0])
'''
Return row 0 and 1:

#use a list of indexes:
print(df.loc[[0, 1]])
'''
'''
Return "day2":

#refer to the named index:
print(df.loc["day2"])
'''
#Example
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
print df
