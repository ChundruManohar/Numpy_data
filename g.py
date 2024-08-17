import numpy as np 

a = np.ndarray(shape=(3,3,3),dtype=int)

val = 1
x = a.shape[0]
y = a.shape[1]
z = a.shape[2]

for i in range(x):
    for j in range(y):
        for k in range(z):
            a[i][j][k] = val
            val = val+1
            
print("array elements ")
print(a)