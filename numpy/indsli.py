import numpy as np

# Indexing and Slicing

# array[index] , 1D array
# array[row, column] , 2D array

"""
Indexing in NumPy allows you to access individual elements or groups of elements from an array.
"""

# 1D ARRAY
arr = np.array([10, 20, 30, 40])
print(arr[0])   # Output: 10
print(arr[-1])  # Output: 40 (last element)

# 2D ARRAY
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[0, 1])  # Output: 2 (row 0, column 1)
print(arr[1, 2])  # Output: 6 (row 1, column 2)

# 3D ARRAY
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr[1, 0, 1])  # Output: 6


"""
Slicing allows you to extract a subarray from a NumPy array using the syntax start:stop:step.

array[start:stop:step]

Note: 

Slicing returns a view (not a copy) of the original array, so modifying the slice will affect the original array.
Use .copy() if you want to create a copy of the sliced array.

"""

# 1D ARRAY
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])    # Output: [20 30 40]
print(arr[:3])     # Output: [10 20 30]
print(arr[::2])    # Output: [10 30 50]
print(arr[::-1])   # Output: [50 40 30 20 10]


# 2D ARRAY
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0:2, 1:3])  # Output: [[2 3] [5 6]]
print(arr[:, 1])      # Output: [2 5 8] (all rows, column 1)
print(arr[1, :])      # Output: [4 5 6] (row 1, all columns)

# 3D ARRAY
arr = np.arange(27).reshape(3, 3, 3)
print(arr[1:, :, :2])  # Slices last two 3x3 matrices, all rows, first two columns


# Boolean Indexing: Select elements based on conditions.

arr = np.array([1, 2, 3, 4, 5])
print(arr[arr > 3])  # Output: [4 5]

# Fancy Indexing: Use arrays of indices to access multiple elements.

arr = np.array([10, 20, 30, 40, 50])
indices = [1, 3, 4]
print(arr[indices])  # Output: [20 40 50]