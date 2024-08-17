import numpy as np
'''a = int(input("enter size? "))
b = np.ndarray(shape=(a),dtype=int)
print("Enter %d a number " %a)
for t in range(a):
    b[t] = int(input())
print("Array elements ",b)'''

c = int(input("Enter a number of rows"))
d = int(input("Enter a numbrer of columns"))

e = np.ndarray(shape=(c,d),dtype=int)
print("Size",e.size)
print("shape",e.shape)
print("Dimension",e.ndim)

