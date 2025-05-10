import numpy as np


"""
NumPy(Numerical Python) is a fundamental library for Python numerical computing.
It provides efficient multi-dimensional array objects and various mathematical functions for 
handling large datasets making it a critical 
tool for professionals in fields that require heavy computation.
"""


# Features in Numpy

# 1. Numpy is a powerful library for numerical computing in Python.
# 2. It provides support for large multi-dimensional arrays and matrices.
# 3. Arrays are stored in contiguous memory locations, enabling faster computations than Python lists
# 4. Numpy provides a wide range of mathematical functions to perform operations on arrays.
# 5. It supports broadcasting, This allows element-wise computations between arrays of different shapes.
#		It simplifies operations on arrays of various shapes by automatically aligning their dimensions without creating new data.
# 6. Numpy is widely used in data science, machine learning, and scientific computing.
# 7. It is often used in conjunction with other libraries like Pandas, Matplotlib, and SciPy.
# 8. NumPy contains routines for linear algebra operations, such as matrix multiplication, decompositions, and determinants.

# Creating a 1D array
x = np.array([1, 2, 3])

# Creating a 2D array
y = np.array([[1, 2], [3, 4]])

# Creating a 3D array
z = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(x)  # [1 2 3]
print(y)  #[[1 2] [3 4]]
print(z)  # [[[1 2] [3 4]] [[5 6] [7 8]]]