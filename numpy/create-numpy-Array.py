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



# --------------------------------------------------------------------------------------------------
"""
linspace() function in NumPy returns an array of evenly spaced numbers over a specified range.
Unlike the range() function in Python that generates numbers with a specific step size.
linspace() allows you to specify the total number of points you want in the array, 
and NumPy will calculate the spacing between the numbers automatically.

# SYNTAX
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

# Parameters:

    start: [optional] start of interval range. By default start = 0
    stop: end of interval range
    num: [int, optional] No. of samples to generate
    retstep: If True, Stop is the last sample By default restep = False
    endpoint: If True, stop is included as the last value. If False, stop is excluded. By default endpoint=True.
    dtype: type of output array
    axis: If start and stop are arrays, axis specifies on what axis will the values be added. If axis = 0, value is added to front, if axis = -1 value is added at the end.

Return Type:

    ndarray
    step : [float, optional], if restep = True

"""
# Example 1: Basic Usage
arr = np.linspace(0, 10, num=5)
print(arr) # [ 0. 2.5 5. 7.5 10.]


# Generate 10 numbers between 0 and 1
array = np.linspace(0, 1, num=10)
print(array) # [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556 0.66666667 0.77777778 0.88888889 1.        ]


# Example 2: Exclude the endpoint
arr = np.linspace(0, 10, num=5, endpoint=False)
print(arr) # [0. 2. 4. 6. 8.]


# Example 3: Include the endpoint
arr = np.linspace(0, 10, num=5, endpoint=True)
print(arr) # [ 0. 2.5 5. 7.5 10.]


# Example 4: Return the step size
arr, step = np.linspace(0, 10, num=5, retstep=True)
print(arr) # [ 0. 2.5 5. 7.5 10.]
print("Step size:", step) # Step size: 2.5


# Example 5: Specifying the data type
arr = np.linspace(0, 10, num=5, dtype=int)
print(arr) # [ 0 2 5 7 10]

# Create a 2D array of 5x5 numbers between 0 and 1
arr = np.linspace(0, 1, num=25).reshape(5, 5)
print(arr) # [[0.   0.04 0.08 0.12 0.16] [0.2  0.24 0.28 0.32 0.36] [0.4  0.44 0.48 0.52 0.56] [0.6  0.64 0.68 0.72 0.76] [0.8  0.84 0.88 0.92 0.96]]

# Example 6: Specifying the axis
arr = np.linspace(0, 10, num=5, axis=-1)
print(arr) # [ 0.   2.5  5.   7.5 10. ]

# ---------------------------------------------------------------------------------------------
"""
 numpy.eye() is a function in the NumPy library that creates a 2D array with ones on the diagonal and zeros elsewhere.
This function is often used to generate identity matrices with ones along the diagonal and zeros in all other positions.

# SYNTAX
numpy.eye(N, M=None, k=0, dtype=<class ‘float’>, order=’C’)

Parameters:
	N: int – Number of rows in the output array.
	M: int, optional – Number of columns in the output array. If not specified, it defaults to N.
	k: int, optional – Index of the diagonal. Default is 0, which refers to the main diagonal. Positive values refer to diagonals above the main diagonal, and negative values refer to diagonals below.
	dtype: data-type, optional – The desired data type of the output array. Default is float.
	order: {‘C’, ‘F’}, optional – Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory.

"""
# Example 1: Basic Usage
identity_matrix = np.eye(3)
print(identity_matrix) # [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]]
# Example 2: Specifying the number of rows and columns
identity_matrix = np.eye(3, 4)
print(identity_matrix) # [[1. 0. 0. 0.] [0. 1. 0. 0.] [0. 0. 1. 0.]]
# Example 3: Specifying a diagonal offset refers to shifting the location of the diagonal filled with 1s within the matrix.
identity_matrix = np.eye(3, k=1)
print(identity_matrix) # [[0. 1. 0.] [0. 0. 1.] [0. 0. 0.]]
# Example 4: Specifying the data type
identity_matrix = np.eye(3, dtype=int)
print(identity_matrix) # [[1 0 0] [0 1 0] [0 0 1]]


# ------------------------------------------------------------------------------------------
"""
Empty array: This array isn’t initialized with any specific values. It’s like a blank page, ready to be filled with data later. 
However, it will contain random leftover values in memory until you update it.

Empty arrays are useful when you want to create an array but don’t have the data ready yet.

# SYNTAX
numpy.empty(shape, dtype=float, order='C')
Parameters:
	shape: int or tuple of int – The shape of the empty array.
	dtype: data-type, optional – The desired data type of the array. Default is float.
	order: {‘C’, ‘F’}, optional – Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory.
"""

# Example 1: Basic Usage
empty_array = np.empty(5)
print(empty_array) # [ 0. 2.5 5. 7.5 10. ]
# Example 2: Specifying the shape
empty_array = np.empty((2, 3))
print(empty_array) # [[0. 0. 0.] [0. 0. 0.]]
# Example 3: Specifying the data type
empty_array = np.empty(5, dtype=int)
print(" first" , empty_array) # [0 4612811918334230528 4617315517961601024 4620130267728707584 4621819117588971520]
# Example 4: Specifying the order
empty_array = np.empty((2, 3), dtype=int, order='F')
print(empty_array) # [[0 0 0] [0 0 0]]


# ------------------------------------------------------------------------------------------
"""
numpy.full() is a function in NumPy that creates a new array of a specified shape and type, filled with a specified value.
This function is useful when you need an array initialized with a specific value, rather than zeros or ones.
# SYNTAX
numpy.full(shape, fill_value, dtype=None, order='C')
Parameters:
	shape: int or tuple of int – The shape of the new array.
	fill_value: scalar – The value to fill the array with.
	dtype: data-type, optional – The desired data type of the output array. If not specified, it defaults to the data type of fill_value.
	order: {‘C’, ‘F’}, optional – Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory.
"""
# Example 1: Basic Usage
full_array = np.full(5, 7)
print(full_array) # [7 7 7 7 7]
# Example 2: Specifying the shape
full_array = np.full((2, 3), 7)
print(full_array) # [[7 7 7] [7 7 7]]
# Example 3: Specifying the data type
full_array = np.full(5, 7, dtype=float)
print(full_array) # [7. 7. 7. 7. 7.]


# ------------------------------------------------------------------------------------------
"""
numpy.meshgrid()– It is used to create a rectangular grid out of two given one-dimensional 
arrays representing the Cartesian indexing or Matrix indexing. 
It is useful for evaluating functions on a grid.

# SYNTAX
numpy.meshgrid(*xi, copy=True, sparse=False, indexing='xy')
Parameters:
	*xi: 1-D arrays – Input arrays.
	copy: bool, optional – If True, the output arrays are always copied. Default is True.
	sparse: bool, optional – If True, a sparse meshgrid is returned. Default is False.
	indexing: {‘xy’, ‘ij’}, optional – Cartesian (‘xy’) or matrix (‘ij’) indexing of output. Default is ‘xy’.
"""
# Example 1: Basic Usage
x = np.array([1, 2, 3])
y = np.array([4, 5])
X, Y = np.meshgrid(x, y)
print("X:\n", X) # [[1 2 3] [1 2 3]]
print("Y:\n", Y) # [[4 4 4] [5 5 5]]
# Example 2: Specifying the indexing
x = np.array([1, 2, 3])
y = np.array([4, 5])
X, Y = np.meshgrid(x, y, indexing='ij')
print("X:\n", X) # [[1 1] [2 2] [3 3]]
print("Y:\n", Y) # [[4 5] [4 5] [4 5]]
# Example 3: Sparse meshgrid
x = np.array([1, 2, 3])
y = np.array([4, 5])
X, Y = np.meshgrid(x, y, sparse=True)
print("X:\n", X) # [[1 2 3]]
print("Y:\n", Y) # [[4 5]]
# Example 4: Using copy parameter
x = np.array([1, 2, 3])
y = np.array([4, 5])
X, Y = np.meshgrid(x, y, copy=False)
print("X:\n", X) # [[1 2 3] [1 2 3]]
print("Y:\n", Y) # [[4 4 4] [5 5 5]]


# --------------------------------------------------------------------------
"""
numpy.exp()– this mathematical function helps the user to calculate the exponential of all the elements in the input array.

The numpy.exp() function is used to calculate the exponential of all elements in the input array.
It computes ( e^x ), where ( e ) is Euler's number (approximately 2.718) and ( x ) is the input value.

# SYNTAX
numpy.exp(array, out = None, where = True, casting = ‘same_kind’, order = ‘K’, dtype = None)

Parameters
x: array-like
Input values for which the exponential is to be calculated.

out: ndarray, None, or tuple of ndarray and None, optional
A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided, a freshly-allocated array is returned.

where: array-like, optional
This condition is broadcast over the input. At locations where the condition is True, the out array will be set to the ufunc result. Elsewhere, the out array will retain its original value.

Returns
out: ndarray
An array with the exponential of each element in the input array



Use Cases
Scientific computations involving exponential growth or decay.
Calculating probabilities in machine learning models like softmax.
Solving mathematical equations involving exponentials.
Notes
The function works element-wise on arrays.
It is highly optimized for performance and is faster than using Python's built-in math.exp() for arrays.
"""

# Example 1: Exponential of a single value
x = 1
result = np.exp(x)
print(result)  # Output: 2.718281828459045

# Example 2: Exponential of an array
arr = np.array([0, 1, 2])
result = np.exp(arr)
print(result)  # Output: [ 1.          2.71828183  7.3890561 ]

# Example 3: Using the `out` parameter
arr = np.array([1, 2, 3])
out = np.zeros_like(arr, dtype=float)
np.exp(arr, out=out)
print(out)  # Output: [ 2.71828183  7.3890561  20.08553692 ]



# ----------------------------------------------------------------------------------
"""
creating a vector in Python using NumPy

A vector is a one-dimensional array that can hold multiple values.


# SYNTAX
Syntax : np.array(list)
Argument : It take 1-D list it can be 1 row and n columns or n rows and 1 column
Return : It returns vector which is numpy.ndarray
"""

# Creating a Vector

# creating a 1-D list (Horizontal) 
list1 = [1, 2, 3] 
  
# creating a 1-D list (Vertical) 
list2 = [[10], 
        [20], 
        [30]] 
  
# creating a vector1 
# vector as row 
vector1 = np.array(list1) 
  
# creating a vector 2 
# vector as column 
vector2 = np.array(list2) 
  
  
# showing horizontal vector 
print("Horizontal Vector") 
print(vector1) # [1 2 3]
  
print("----------------") 
  
# showing vertical vector 
print("Vertical Vector") 
print(vector2)
"""
[[10]
 [20]
 [30]]
 """

 # Basic Arithmetic operation on vectors

 # creating a 1-D list (Horizontal) 
list1 = [5, 6, 9] 
  
# creating a 1-D list (Horizontal) 
list2 = [1, 2, 3] 
  
# creating first vector 
vector1 = np.array(list1) 
  
# printing vector1 
print("First Vector          : " + str(vector1)) # [5 6 9]
  
# creating second vector 
vector2 = np.array(list2) 
  
# printing vector2 
print("Second Vector         : " + str(vector2)) # [1 2 3]
  
# adding both the vector 
# a + b = (a1 + b1, a2 + b2, a3 + b3) 
addition = vector1 + vector2  
  
# printing addition vector 
print("Vector Addition       : " + str(addition)) # [6 8 12]
  
# subtracting both the vector 
# a - b = (a1 - b1, a2 - b2, a3 - b3) 
subtraction = vector1 - vector2 
  
# printing addition vector 
print("Vector Subtraction   : " + str(subtraction)) # [4 4 6]
  
# multiplying  both the vector 
# a * b = (a1 * b1, a2 * b2, a3 * b3) 
multiplication = vector1 * vector2 
  
# printing multiplication vector 
print("Vector Multiplication : " + str(multiplication)) # [ 5 12 27]
  
# dividing  both the vector 
# a / b = (a1 / b1, a2 / b2, a3 / b3) 
division = vector1 / vector2 
  
# printing division vector 
print("Vector Division       : " + str(division))  # [5. 3. 3.]


# Vector Dot Product
# The dot product of two vectors is the sum of the products of their corresponding components.

# creating a 1-D list (Horizontal) 
list1 = [5, 6, 9] 
  
# creating a 1-D list (Horizontal) 
list2 = [1, 2, 3] 
  
# creating first vector  
vector1 = np.array(list1) 
  
# printing vector1 
print("First Vector  : " + str(vector1))  # [5 6 9]
  
# creating second vector 
vector2 = np.array(list2) 
  
# printing vector2 
print("Second Vector : " + str(vector2)) # [1 2 3]
  
# getting dot product of both the vectors 
# a . b = (a1 * b1 + a2 * b2 + a3 * b3) 
# a . b = (a1b1 + a2b2 + a3b3) 
dot_product = vector1.dot(vector2) 
  
# printing dot product 
print("Dot Product   : " + str(dot_product)) # 44

# Vector-Scalar Multiplication
# The multiplication of a vector by a scalar is the multiplication of each component of the vector by the scalar.

# creating a 1-D list (Horizontal) 
list1 = [1, 2, 3] 
  
# creating first vector  
vector = np.array(list1) 
  
# printing vector1 
print("Vector  : " + str(vector)) # [1 2 3]
  
# scalar value  
scalar = 2
  
# printing scalar value 
print("Scalar  : " + str(scalar))  # 2
   
# getting scalar multiplication value 
# s * v = (s * v1, s * v2, s * v3) 
scalar_mul = vector * scalar 
  
# printing dot product 
print("Scalar Multiplication : " + str(scalar_mul)) # [2 4 6]



# ---------------------------------------------------------------------------------------------

#  Numpy fromrecords() method
# The fromrecords() method in NumPy is used to create a structured array from a list of tuples or records.
# This method is particularly useful when you have a collection of records, each with the same structure, 
# and you want to convert them into a NumPy array for efficient processing.

# SYNTAX
# numpy.fromrecords(recList, dtype=None, shape=None, aligned=False, byteorder=None)
"""
Parameters:
    recList: A list of tuples or structured data to be converted into a structured NumPy array.
    dtype (optional): The data type of the resulting structured array. If not provided, NumPy will infer the type from the input data.
    shape (optional): Shape of the output array. Defaults to one-dimensional.
    aligned (optional): If True, aligns fields to their natural alignment.
    byteorder (optional): Specifies the byte order of the output array.
	"""

	# Define a list of records
records = [(1, 'Alice', 25.5), (2, 'Bob', 30.0), (3, 'Charlie', 28.0)]

# Define the data type
dtype = [('id', 'i4'), ('name', 'U10'), ('age', 'f4')]

# Create the structured array
structured_array = np.array(records, dtype=dtype)

print(structured_array) # [(1, 'Alice', 25.5) (2, 'Bob', 30. ) (3, 'Charlie', 28. )]

# Access the 'name' field
print(structured_array['name']) # ['Alice' 'Bob' 'Charlie']

# Access the 'age' field
print(structured_array['age']) # [25.5 30.  28. ]