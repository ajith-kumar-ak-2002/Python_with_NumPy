import numpy as np

#Array Joining
# Joining means combining multiple arrays into one.
# NumPy provides different joining functions:
# np.concatenate()
# np.stack()
# np.hstack()
# np.vstack()


#np.concatenate()
a = np.array([1,2,3])
b = np.array([4,5,6])
print("concatenated arrays: ", np.concatenate((a, b)))
c = np.array([[1,2], [3,4]])                            #axis=0 → Join vertically (↓ rows)
d = np.array([[5,6], [7,8]])                            #axis=1 → Join horizontally (→ columns)
print("concatenated arrays: \n" , np.concatenate((c,d), axis=0))


#np.stack()
s1 = np.array([1,2,3])
s2 = np.array([4,5,6])
stacked = np.stack((s1, s2))
print("Stacked Array: \n", stacked)
print(stacked.shape)
s3 = np.array([[1,2,3]])
s4 = np.array([[4,5,6]])
result = np.stack((s3,s4))
print("2D Stacked Array: \n", result)
print(result.shape)


#np.hstack()
h1 = np.array([1,2,3])
h2 = np.array([4,5,6])
print("hstack: ", np.hstack((h1,h2)))
#np.vstack()
v1 = np.array([1,2,3])
v2 = np.array([4,5,6])
print("vstack: \n", np.vstack((v1, v2)))





#Array Splitting
# np.split()
# np.hsplit()
# np.vsplit()

#np.split()
np1 = np.array([[1,2,3,5],
                [4,5,6,9]])
result = np.split(np1, 2, axis=1)
print("Split Results: " ,result)

#np.hsplit
hs = np.array([[1,2,3,4],
               [5,6,7,8]])

r1 = np.hsplit(hs, 2)
print("Hsplit Results: ", r1)

#np.vsplit
vs = np.array([[1,2,3,4],
               [5,6,7,8]])
r2 = np.vsplit(vs , 2)
print("Vsplit Resluts: ", r2)





#Sorting Arrays
# np.sort() → Returns sorted array
# np.argsort() → Returns indices to sort the array

arr = np.array([2,5,1,30,20])
print("Sort: ", np.sort((arr)))
# Indices that would sort the array
print("sort: ", np.argsort((arr)))

#Sorting 2D Arrays
# axis=0 → Sorts by columns
# axis=1 → Sorts by rows
matrix = np.array([[6,2,8],
                   [9,1,5]])
print("sort: \n", np.sort((matrix), axis=1))
print("sort: \n", np.sort((matrix), axis=0))