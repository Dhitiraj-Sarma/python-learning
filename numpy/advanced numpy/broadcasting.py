import numpy as np

prices = np.array([100, 200, 300])
discount = 10

final_prices = prices - (prices * discount/100)

print(final_prices)

# Broadcasting in NumPy
"""
Broadcasting is a powerful feature in NumPy that allows arrays of different shapes to be used together in arithmetic operations. It automatically expands the smaller array so that it matches the shape of the larger array, without making unnecessary data copies.

How Broadcasting Works
	1. If two arrays have different shapes, NumPy compares their shapes element-wise, starting from the trailing (rightmost) dimension.
	2. Two dimensions are compatible when:
		a. They are equal, or
		b. One of them is 1
	3. If the shapes are not compatible, broadcasting will fail with a ValueError.
Broadcasting Rules
	1. If the arrays do not have the same number of dimensions, prepend 1s to the shape of the smaller array.
	2. Compare the shapes element-wise. Dimensions are compatible if they are equal or one of them is 1.
	3. The resulting array shape is the maximum along each dimension.
Benefits of Broadcasting
	1. Enables vectorized operations, making code more concise and efficient.
	2. Avoids explicit loops and unnecessary memory usage.
Limitations
	1. Not all shapes are compatible for broadcasting.
	2. If shapes are not compatible, NumPy raises a ValueError.

"""

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
result = arr + 5
print(result)
# Output: [ 6 7 8 9 10 11 12 13 14]

matrix = np.array([[1, 2, 3], [4, 5, 6]]) # 2x3 matrix
vector = np.array([10, 20, 30]) #1d array

result = matrix + vector 
print(result)
# [[11 22 33]
#  [14 25 36]]


a = np.array([[1], [2], [3]])  # Shape: (3, 1)
b = np.array([10, 20, 30])     # Shape: (3,)
result = a + b
print(result)
# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

arr1 = np.array([[1, 2, 3], [4, 5, 6]])  #shpae(2, 3)
arr2 = np.array([1, 2]) # shape(2,)

arr3 = arr2.reshape(2, 1)

print(arr1 + arr3)