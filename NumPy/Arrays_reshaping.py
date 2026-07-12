import numpy as np

#reshape
#1D Converts into 2D
r1 = np.arange(66)
print("Original Array:", r1)
r2 = r1.reshape(-6,6)                   # # Using -1 to auto-calculate dimension
print("Reshaped After (2*3): \n",r2)


#flatten
f = np.array([[1,2], [3,4]])                #2D Converts into One 1D its creates a copy 
fl = f.flatten()
fl = np.append(fl , 5)
print("Original array:\n", f)
print("flatten array: ", fl)


#ravel
arr = np.array([[10, 20], [30,40]])
r = arr.ravel()                         #if User Change in copyed file also in original also may change 
r[0] = 100
print(arr)
print(r)


#np.newaxis
new = np.array([1,2,3])
row = new[np.newaxis, :]
col = new[:, np.newaxis]
print("Row: ", row)
print("Row Shape: ", row.shape)
print("Column: \n" ,col)
print("Column Shape: ", col.shape)



#resize                     # Resizes array even if shape doesn’t match. It repeats data if needed.
a = np.array([1,2,3])
b = np.resize(a, (2,4))
print(b)