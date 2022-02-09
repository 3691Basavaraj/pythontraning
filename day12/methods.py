# describe()
import pandas as pd

dict = {
    "name": ['atul', 'rohan', 'pavan'],
    "marks": [20, 30, 40],
    "city": ['bangalore', 'belgaum', 'hubli'],
    "pincode": [56, 45, 67]
}
df = pd.DataFrame(dict)
print(df)
# print(df.describe())  # gives the description of numerical values

# print(df.sum(axis=1)) #returns sum of numerical according to given axis
# print(df.mean(axis=0))  # return mean value of existing numerical value
# print(df.max(axis=1)) #prits maximum from the columns
# print(df.min(axis=1))  # prints minimum from the colum
# print(df.shape)  # returns the matrix of the dataframe
# df1 = df.drop(['name', 'city'], axis=1)#delets rows or columns according to axis
# print(df1)
#print(df.loc[1, 'marks'])  # Accessing rows and columns using loc method
#print(df.iloc[1,2]) #Accessing rows and columns using iloc method
