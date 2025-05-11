import numpy as np

print(np.__version__) # Checking the version of numpy

# creating array with numpy

arr = np.array([1, 2, 3, 4, 5])

print(arr)  # [1 2 3 4 5]
print(type(arr)) # <class 'numpy.ndarray'>


# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

# Using a tuple to create a array

arr = np.array((1, 2, 3, 4, 5))

print(arr)  # [1 2 3 4 5]


# Creating a 0D array
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

arr = np.array(42)

print(arr) # 42

# Creating a 1D array
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

arr = np.array([1, 2, 3, 4, 5])

print(arr)  # [1 2 3 4 5]


# Creating a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr) # [[1 2 3] [4 5 6]]

# Creating a 3D array

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr) # [[[1 2 3] [4 5 6]] [[1 2 3] [4 5 6]]]



# Check Number of Dimensions
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim) # 0
print(b.ndim) # 1
print(c.ndim) # 2
print(d.ndim) # 3

# Higher Dimensional Arrays

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr) # [[[[[1 2 3 4]]]]]
print('number of dimensions :', arr.ndim) # 5



# -------------------------------------------------------------------------------------------------------

# NUMPY METHODS
# numpy.arange() function creates an array of evenly spaced values within a given interval.
# It is similar to Python’s built-in range() function but returns a NumPy array instead of a list.

# SYNTAX

# numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)

"""
    start (optional): The starting value of the sequence. Default is 0.
    stop (required): The endpoint of the sequence, exclusive.
    step (optional): The spacing between consecutive values. Default is 1.
    dtype (optional): The desired data type of the output array.
"""

arr= np.arange(5 , 10)
print(arr) # [5 6 7 8 9]

sequence = np.arange(10)
print("Basic Sequence:", sequence) #  [0 1 2 3 4 5 6 7 8 9]

# Creating a sequence of floating-point numbers from 0 to 1 
# with a step size of 0.2 using np.arange()
sequence = np.arange(0, 1, 0.2)
print("Floating-Point Sequence:", sequence) #  [0.  0.2 0.4 0.6 0.8]

# Creating a sequence of numbers from 0 to 20 
sequence = np.arange(0, 20, 3)

# Filtering the sequence to include only values greater than 10
filtered = sequence[sequence > 10]
print("Filtered Sequence:", filtered) # [12 15 18]



# -------------------------------------------------------------------------------------------------------

# numpy.zeros() function creates a new array of specified shapes and types, filled with zeros.
# It is beneficial when you need a placeholder array to initialize variables or store intermediate results.
# We can create 1D array using numpy.zeros().

# SYNTAX
# numpy.zeros(shape, dtype = None, order = ‘C’)

"""
Parameters:

    shape: integer or sequence of integers – Defines the shape of the new array. Can be a single integer or a tuple.
    dtype: optional, default is float – The data type of the returned array. If not specified, the default is float.
    order: {‘C’, ‘F’} – Specifies the memory layout order:
        C-order: C-contiguous order means the last index varies the fastest. It is optimal for row-wise operations.
        F-order: FORTRAN-contiguous order means the first index varies the fastest. It is optimal for column-wise operations.

Return Value

    numpy.zeros() returns a new array filled with zeros, based on the specified shape and type.
"""

arr = np.zeros(5)
print(arr) # [0. 0. 0. 0. 0.]

# Creating a 2D array with 3 rows and 4 columns
arr = np.zeros((3, 4))

print(arr) # [[0. 0. 0. 0.] [0. 0. 0. 0.] [0. 0. 0. 0.]]

# Create an array of tuples with zeros
d = np.zeros((2, 2), dtype=[('f', 'f4'), ('i', 'i4')])
print(d) # [[(0., 0) (0., 0)] [(0., 0) (0., 0)]]


# Create a 2x3 array in C-order
e = np.zeros((2, 3), order='C')
print("C-order array:", e) # [[0. 0. 0.] [0. 0. 0.]]

# Create a 2x3 array in F-order
f = np.zeros((2, 3), order='F')
print("F-order array:", f) # [[0. 0. 0.] [0. 0. 0.]]


# -----------------------------------------------------------------------------------------
# To create an array filled with all ones, given the shape and type of array, we can use numpy.ones() method of NumPy library in Python.


array = np.ones(5)
print(array) # [1. 1. 1. 1. 1.]

# Create a 2D array of ones (3 rows, 4 columns)
ones_array_2d = np.ones((3, 4))
print(ones_array_2d) # [[1. 1. 1. 1.] [1. 1. 1. 1.] [1. 1. 1. 1.]]

# Create an integer array of ones with 4 elements
ones_int_array = np.ones(4, dtype=int)
print(ones_int_array) # [1 1 1 1]

# Create a 3D array of ones with shape (2, 3, 4)
ones_array_3d = np.ones((2, 3, 4), dtype=int)
print(ones_array_3d) # [[[1 1 1 1] [1 1 1 1] [1 1 1 1]] [[1 1 1 1] [1 1 1 1] [1 1 1 1]]]