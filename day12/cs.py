'''
A CSV (Comma Separated Values) format is one of the most simple and common ways to store tabular data.
To represent a CSV file, it must be saved with the .csv file extension.
'''
# To read a CSV file
import pandas as pd
import numpy as np

#df1 = pd.read_csv('/home/basavaraj/Desktop/Tibil/nba.csv')  # to import a csv file
#print(df1.head(3))

# to write a CSV from data frame

#df1.to_csv('/home/basavaraj/Desktop/Tibil/nba1.csv')

'''dict = {
    "name": ['atul', 'rohan', 'pavan'],
    "marks": [20, 30, 40],
    "city": ['bangalore', 'belgaum', 'hubli']
}
df = pd.DataFrame(dict)'''

#df.to_csv('/home/basavaraj/Desktop/Tibil/sample1.csv',index=False)

# Slicing and indexing

# Slicing rows

#df2 = df.iloc[0:2, 0:]
#print(df2)

# slicing columns

#df3 = df.iloc[:, :]
#print(df3)
