import pandas as pd
import numpy as np

# df1 = pd.read_csv('/home/basavaraj/Desktop/Tibil/sample.csv')  # to import a csv file
df2 = pd.DataFrame(np.random.rand(10, 5), index=np.arange(10))  # to print random data frame of float values
# print(df1)
# print(df2)
# print(type(df2))  # to determine the type of table created.
# df2[0][0] = "Basavaraj" #to change item in the dataframe using index
# df2.index = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10  # to change the index of the rows
# print(df2)
# df2.columns = list("ABCDE")  # to change the colum name
# print(df2)
# df3 = df2.loc[[1, 4], [1, 2]]  # Accessing rows and columns using loc method
# print(df3)
# df4 = df2.iloc[[1, 9], [1, 3]]  # Accessing rows and columns using loc method
# print(df4)
#df5 = df2.drop([3], axis=1) # drops the specified row or colum
#print(df5)
#df2.loc[[0]] = 'Tibil'
#print(df2)
'''new_row = {0: 'A', 1: 87, 2: 92, 3: 97, 4: 67}  # append row to the dataframe
new = df2.append(new_row, ignore_index=True)  # append row  to the dataframe
print(new)'''
#new_col = [1, 2, 3, 4, 5, 6, 7, 8, 9,8] # append colum to the dataframe
#df2[5] = new_col # add colum to the dataframe
#print(df2)

