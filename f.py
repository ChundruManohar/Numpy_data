import numpy as np  

a = int(input("Enter no of rows "))
b = int(input("Enter no of columns "))
ma = np.ndarray(shape=(a,b),dtype=int)
print("enter no of %d elements "%(a*b))
for i in range(a):
    for j in range(b):
        ma[i][j]=int(input())

print(ma)