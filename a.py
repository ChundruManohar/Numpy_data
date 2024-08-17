import numpy 

my_list = [10,20,30,40,50]

arr = numpy.array(my_list)
print(arr)
print(type(arr))
print("Size: ", arr.size)
print("Datatype: ",arr.dtype)
print("Dimension: ",arr.ndim)
print("Shape: ",arr.shape)

matrix = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
print("size: ",matrix.size)
print('Datatype: ',matrix.dtype)
print('dimension ',matrix.ndim)
print('shape: ',matrix.shape)



