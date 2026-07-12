import numpy as np 

#1D Array in NumPy
a = np.array([1, 2, 3, 4])

print(a)
print(a.size)
print(a.shape)
print(a.nbytes)
print(a.dtype)
print(a.itemsize)

#2D Array in NumPy

b = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(b)
print("Size of the array: ", b.size)
print("Shape of the array: ", b.shape)
print("Dimensions of the array: ", b.ndim)
print("Datatype: ", b.dtype)
print("Individual Item Size: ", b.itemsize)
print("Total Bytes of the array: ", b.nbytes)
