import numpy as np

"""
Vectorization refers to performing operations on entire arrays (or large chunks of data) at once, rather than using explicit Python loops.
 NumPy achieves this using optimized C code, making operations much faster and more concise.


Benefits of Vectorization
Speed: Operations are performed in compiled code, much faster than Python loops.
Simplicity: Code is shorter and easier to read.
Memory Efficiency: No need for explicit loops or intermediate lists.


Common Vectorized Operations
Arithmetic: +, -, *, /
Mathematical functions: np.sin(), np.exp(), np.sqrt(), etc.
Comparisons: arr1 > arr2, arr == value
Aggregations: np.sum(), np.mean(), etc.

"""

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = arr1 + arr2
print(result)


arr = np.array([10, 20, 30])
multiplied = arr * 3
print(multiplied)


# 2D array

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Element-wise addition
result = arr1 + arr2  # [[6 8] [10 12]]

# Scalar multiplication
multiplied = arr1 * 2  # [[2 4] [6 8]]

# 3d array

arr1 = np.arange(8).reshape(2, 2, 2)
arr2 = np.ones((2, 2, 2))

# Element-wise addition
result = arr1 + arr2
# result shape: (2, 2, 2)

# Scalar multiplication
multiplied = arr1 * 10