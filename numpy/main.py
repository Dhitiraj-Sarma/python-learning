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





# Using Numpy Functions:
#	NumPy provides convenient methods to create arrays initialized with specific values like zeros and ones:



# Creating an array of zeros
zeros_array = np.zeros((2, 3))  # 2 rows, 3 columns
print(zeros_array)  # [[0. 0. 0.] [0. 0. 0.]]



# Creating an array of ones
ones_array = np.ones((3, 2))  # 3 rows, 2 columns
print(ones_array)  # [[1. 1.] [1. 1.] [1. 1.]]



# Creating an array with a range of values
array_range = np.arange(0, 10, 2) # Start at 0, end at 10, step by 2
print(array_range)  # [0 2 4 6 8]






# Create Numpy Arrays Using Lists or Tuples
# You can create NumPy arrays from Python lists or tuples using the np.array() function:

# Creating a NumPy array from a list
my_list = [1, 2, 3, 4, 5]
numpy_array = np.array(my_list)
print(numpy_array) # [1 2 3 4 5]
# Creating a NumPy array from a tuple
my_tuple = (6, 7, 8, 9, 10)
numpy_array_from_tuple = np.array(my_tuple)
print(numpy_array_from_tuple) # [ 6  7  8  9 10]





# Creating an array with values that are evenly spaced over a specified interval
filled_array = np.full((2, 2), 7)  # 2x2 array filled with 7
print(filled_array)  # [[7 7] [7 7]]

# Creates an array with values that are evenly spaced within a given range.
# The np.linspace() function generates an array of evenly spaced values over a specified range.
# It takes three arguments: start, stop, and num (number of samples).
# The start and stop values define the range, and num specifies how many values to generate.
# For example, to create an array with 5 evenly spaced values between 0 and 1:

linspace_array = np.linspace(0, 1, 5)  # 5 values between 0 and 1
print(linspace_array)  # [0.   0.25 0.5  0.75 1.  ]