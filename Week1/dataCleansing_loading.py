import pandas as pd # Importing the library
import numpy as np
df = pd.read_csv('D:/MS/Data Analytics Lab/Week1/Umbrella.csv') # reading the CSV file

df = df.round(3) # Truncating to 3 decimal places

count = 0 
for i in df.duplicated(): # Checking for duplicates in the DataSet
    if i is True:
        count+=1
print("Number of Duplicate Coordinates: ",count) 

# Creation of Sparse Matrix

# To scale the values from [1 - 100] -> [1 - 1000]
df['X1'] = (df['X'] * 10).astype(int)
df['Y1'] = (df['Y'] * 10).astype(int)

# Creating a matrix of 1000 x 1000

matrix = np.zeros([1000,1000],dtype=int)
for index,row in df.iterrows():
    matrix[df['X1'],df['Y1']]=1
print(matrix)

df.to_csv("Umbrella_updated.csv",columns=["X1","Y1"],index=False)