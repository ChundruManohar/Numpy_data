import numpy as np

a = np.array([10,20,30,40,50])
print(a)
print(a.ndim)
print(a.size)

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print()
# [row_low:row_upper,col_low:col_upper]

c =b[:,:]
print(c)
d = b[0:2,0:2]

print(d)
e = b[1:3,1:3]
print(e)
print()
f =b[1:3,0:2]
print(f)
print()
g = b[0:2,1:3]
print(g)



