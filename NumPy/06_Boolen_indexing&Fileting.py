import numpy as np


#Basic Boolean Indexing

# Create a simple array
a = np.array([1,2,3,4,5,6,7,8,9,10])
print("Original index: ", a)
# Get all values greater than 5
b = a[a < 5]
print(b)
# See the boolean mask
c = a > 5
print(c)


#Multiple Conditions
# Combine conditions using & (AND), | (OR), ~ (NOT)
# Values between 3 and 7 (AND condition)
between = a[(a >=3 ) & (a <= 7)]
print("Between 3 and 7: ", between)
# Values less than 3 OR greater than 7 (OR condition)
outside = a[(a < 3) | (a > 7)]
print("<3 or >7: ", outside)
# Values NOT equal to 5 (NOT condition)
not_five = a[~(a == 5)]
print("Not Equal to 5: ", not_five)


#where() Function
# Find indices where values > 5
indices = np.where(a >5)
print("Indices Where : ", indices[0])
print("Value at Where indices: ", a[indices])
## Replace values: if > 5, make it 100, else keep original
replaced = np.where(a > 5,100 , a)
print("After Replacement: ", replaced)


#Filtering 2D Arrays
# Create a 2D array
matrix = np.array([[1,2,3,],
                   [4,5,6],
                   [7,8,9]])
print("original Martix")
print(matrix)
# Get all values > 5 (flattened)
high_value = matrix[matrix > 5]
print("\nValues > 5: ", high_value)
# Keep only rows where first column > 3
row_fliter = matrix[matrix[:, 0] >3 ]
print("\nRows Where first column >3")
print(row_fliter)




#  Temperature data with errors
temperature = np.array([22.5, 23.1, -999, 24.3, 150, 23.8, 22.9])
print("Temperature: ", temperature)

# Remove invalid readings (-999 and values > 50)
valid_temp = temperature[(temperature > 0) & (temperature<50)]
print("valid Temperature: ", valid_temp)
print(f"Removed {len(temperature) - len(valid_temp)} Invalid readings")

# Calculate statistics on clean data
print(f"Average Temperature: {temperature.mean():.1f}°C")