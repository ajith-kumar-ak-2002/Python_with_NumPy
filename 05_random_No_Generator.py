import numpy as np

#rand
# Create 1D array with 5 random decimal numbers
rand_float = np.random.rand(5)
print("Random Decimal Numbers: ", rand_float)
# Create 2D array (2 rows, 3 columns) of random decimals
rand_float1 = np.random.rand(2,4)
print("2D Array: \n", rand_float1)


#randint
# Create 1D array with 5 random decimal numbers
rand_int = np.random.randint(1, 10 , size=5)
print("Integer Value: ", rand_int)
# Create 2D array (2 rows, 3 columns) of random decimals
rand_int1 = np.random.randint(10 , size=(3,3))
print("2D Integer Value: \n",rand_int1)


#randn
# Create 5 natural-looking random numbers
random_value = np.random.randn(5)
print("Natural random Values: ", random_value)
# Create a 2x3 table of such numbers
random_value_2D = np.random.randn(2, 3)
print("2D Random Value: \n", random_value_2D)



#random.seed
np.random.seed(43)
print("First time: ", np.random.rand(3))
np.random.seed(43)
print("Same Result again: ", np.random.rand(3))



#random.choice
# Pick 5 random values from a list
choices = np.random.choice([10, 20, 30, 40], size=5)
print("Choice (Can Repet): ", choices)
# Pick 3 different values (no repeat)
unique_choice = np.random.choice([1,2,3,4,5], size=5 , replace=False)
print("Unique Picks: ", unique_choice)