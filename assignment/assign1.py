import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/basavaraj/Desktop/Tibil/cars.csv')
# print(df.shape)
'''print('Bar plot for CAR vs MPG')
plt.bar(df['Car'], df['MPG'] )
plt.title("BAR Plot for car vs MPG")
plt.xlabel('Car')
plt.ylabel('MPG')
plt.show()'''

'''
print(' Bar plot for CAR vs Cylinders')
plt.bar(df['Car'], df['Cylinders'],  width=0.4)
plt.title("BAR Plot for car vs Cylinders")
plt.xlabel('Car')
plt.ylabel('Cylinders')
plt.show()
'''

'''print('plot for CAR vs Displacement')
plt.plot(df['Car'], df['Displacement'])
plt.title(" Plot for car vs Cylinders")
plt.xlabel('Car')
plt.ylabel('Displacement')
plt.show()'''

'''print('plot for CAR vs Horsepower')
plt.plot(df['Car'], df['Horsepower'])
plt.title(" Plot for car vs Horsepower")
plt.xlabel('Car')
plt.ylabel('Horsepower')
plt.show()'''


'''print(' Scatter plot for CAR vs Weight')
plt.scatter(df['Car'], df['Weight'])
plt.title(" Plot for car vs Weight")
plt.xlabel('Car')
plt.ylabel('Weight')
plt.show()'''


'''print(' Scatter plot for CAR vs Acceleration')
plt.scatter(df['Car'], df['Acceleration'])
plt.title(" Plot for car vs Acceleration")
plt.xlabel('Car')
plt.ylabel('Acceleration')
plt.show()'''
'''print('Histogram plot for CAR vs Model')
plt.hist(df['Car'], df['Model'])
plt.title(" Plot for car vs Model")
plt.xlabel('Car')
plt.ylabel('Model')
plt.show()'''

'''print(' Bar plot for CAR vs Origin')
plt.barh(df['Car'], df['Origin'], color='#F08080' )
plt.title(" Plot for car vs Origin")
plt.xlabel('Car')
plt.ylabel('Origin')
plt.show()
'''
