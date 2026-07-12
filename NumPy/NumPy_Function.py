import numpy as np 

#NumPy Functions for array Creation 

#np.array
    #1D Array
a = np.array([1,2,3,4,5])
print("1D Array: ", a)
    #2D Array
b = np.array([[10,20,30], [40,50,60]])
print("2D Array: \n", b)


#np.zeros
    #1D Zeroes
z1 = np.zeros(5)
print("1D Zeros: ", z1)
print("Data type: ", z1.dtype)
    #2D Zeroes
z2 = np.zeros((2,3) , dtype=int)
print("2D Zeroes: \n", z2)
print("Converted data type: ", z2.dtype)


#np.ones
    #1D ones
o1 = np.ones(4)
print("Ones 1D: ", o1)
    #2D Ones
o2 = np.ones((3,4) , dtype=int)
print("2D Ones: \n", o2)


#np.full
    #1D Full
f1 = np.full(4, 8)
print("Full 1D: ", f1)
    #2D Full
f2 = np.full((2,2), 3.14)
print("Full 2D: \n", f2)


#np.arange          np.arange(start, stop, step)
    #1D Arange
r1 = np.arange(5)
print("0 to 4: ", r1)
    #2D Arange
r2 = np.arange(0,10,2)
print("2D Arange : \n", r2)


#np.linspace
# Syntax ----- np.linspace(start, stop, num=50, endpoint=True, retstep=False) 
#start – starting value
#stop – ending value
#num – how many values you want
#endpoint=True – include stop value or not
#retstep=True – also return spacing between values

    #retstep Linspace
l1 = np.linspace(1,10,3 , retstep=True)         #If False Not Return spacing between values
print("5 Values from 1 to 10: " , l1)
    #endpoint Linspace 
l2 = np.linspace(0, 1, 4, endpoint=False)       #If True 1 Also Written
print("4 Values Between 0 and 1: ", l2)


#np.eye ( Creates an identity matrix where diagonal elements are 1, rest are 0 )
e = np.eye((3) , dtype=int)
print("Identity matrix (3x3): \n", e)