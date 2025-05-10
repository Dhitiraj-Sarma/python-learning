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