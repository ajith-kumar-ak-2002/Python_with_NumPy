import numpy as np

#1D Indexing in NumPy

arr = np.array([1,2,3,4,5,6])

print("Print First Element: ", arr[0])
print("Print Second Element: ", arr[1])
print("Print Last Element: ", arr[-1])


#2D Indexing in NumPy

arr2 = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

print(arr2[0] [1])
print(arr2[1] [2])
print(arr2[2] [1])
# OR using single bracket with comma
print(arr2[0, 2])



#1D Slicing in NumPy

sli = np.array([6, 7, 8, 9, 10])

print("sli[0:4]: ", sli[0:4])
print("sli[:3]: ", sli[:3])
print("sli[2:]: ", sli[2:])
print("sli[::2]: ", sli[::2])

#2D Slicing in NumPy

sli2 = np.array([[10, 20, 30],
                 [50, 60, 40],
                 [20, 10, 90]])

# Slice rows 0 to 2 (not including 2), columns 0 to 2
print(sli2[0:2 , 0:2])

#All rows, fisrt column
print(sli2[:, 0])

#second row , all columns
print(sli2[1, :])

#all rows , Last Column
print(sli2[: , -1])