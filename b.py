import numpy as np


a = np.array([10,20,30,40,50])

for i in a:
    print(i,end=" , ")
print()
    
    
b = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(b)

for ele in b:
    for j in ele:
        print(j,end=" ")
    print()
    
    