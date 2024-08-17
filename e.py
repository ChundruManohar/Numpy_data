import numpy as np

arr = np.ndarray(shape=(5),dtype=int)

print(arr.size)
print(arr.shape)
print(arr.ndim)
print(arr.dtype)

b = np.ndarray(shape=(5), dtype=int)

c = b.size
print("Enter %d numbers" %c )
for  i in range(c):
    b[i] = int(input())
print('Elements are ',b)
    