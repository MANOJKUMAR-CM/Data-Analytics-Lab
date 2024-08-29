import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("D:/MS/Data Analytics Lab/Week1/Umbrella_updated.csv")


# Creating a matrix of 1000 x 1000

matrix = np.zeros([1000,1000],dtype=int)
for index,row in df.iterrows():
    matrix[df['X1'],df['Y1']]=1

matrix = matrix.transpose()
matrix = np.fliplr(matrix)
matrix = matrix.transpose()
matrix_270 = np.fliplr(matrix)

X=[]
Y=[]
for x in range(0,1000):
    for y in range(0,1000):
        if(matrix_270[x,y]==1):
            X.append(x)
            Y.append(y)

df['X2']=X
df['Y2']=Y
plt.scatter(df['X2'],df['Y2'])
plt.title('Scatter Plot of Matrix Flipped')
plt.xlabel('X2')
plt.ylabel('Y2')
plt.show()

            