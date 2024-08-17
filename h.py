import numpy as np 
# [0 1 2 3 4] output 5 is not included 

a = np.arange(5)
print(a)
#0 is include 27 excluded
b = np.arange(0,27)
print(b)

#ndarray no of dimensions array 

a = np.array([1,2,3,4,5])
print(a)
print(a[3])

#2d array 
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b.ndim)
print(b[1][2])


#shape of the array 

a = np.array([1,2,3])
print(a.shape)
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print("shape of the array: ",a.shape)

#data types in python 

a = np.array([1.1,2.2,3.3],dtype=np.int32)

print(a.dtype)
print(a)

#size 
ab = np.zeros((2,3,4))
print(ab)
print("total elements ",ab.size)#2*3*4 = 24
print(ab.dtype)

a = np.ones((2,3,4,5))
print(a.dtype)
print(a.size)
print(a.ndim)
property(a.shape)
print(a)

#iteam size bytes 
a = np.array([1,2,3])
print("total byes of each element ",a.itemsize)
print(a.dtype)

#data type 
a = np.array([1,3,4],dtype=np.int32)
print(a.dtype)
b = np.array([1.1,2.2,3.3],dtype=np.float32)
print(b.dtype)
# int32 occupice less space compaired int64
# toal sum related float64 exactly value compare float32

#np.zeros,np.ones,np.full:
#np.zeros(shape,dtype=float32)

a = np.zeros((2,3))
print(a) 
b = np.ones((3,3))
print(b)
c = np.ones((3,2))
print(c)

# arthmatic operations 
a = np.add([1,2,3],[4,5,6])
print("addition ",a)

b = np.subtract([1,2,3],[4,5,6])
print(b)

c = np.multiply([1,2,3],[4,5,6])
print(c)

d = np.divide([10,12,14],[2,3,2])
print("divided",d)

e = np.power([2,3,4],[2,3,2])
print("exponential :",e)

#relational operator 

a = np.array([1,2,3,4])
b = np.array([1,2,3,5])

print("equal ",a==b)

print("not equal ", a != b)


#scilicing [start:stop:step]

a = np.array([1,2,3,4,5,6,26])
print(a[5])
print(a[-1])
print(a[1:4])
print(a[::-1])
print()
print(a[1:])
print(a[:5])
print(a[::3])
print()
print()
# 2d array 
a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a[-1:-1])
print(a)
print(a[2][2])
print(a[1][2])
print(a[0 , 2])

print(a[1:3,1:3])
print()
print(a[0:2,0:2])
print()

print(a[0:2,1:3])

a[0:2,1:3]=[[10,20],[30,40]]
print(a)


#c mass level indexing 




print(a[-1,-1])