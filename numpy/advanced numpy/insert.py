import numpy as np
"""
np.insert(array, index, value, axis=None)
array: The original array.
index: The position(s) where new values are to be inserted.
values: The values to insert. The shape must match the array except along the insertion axis.
axis: The axis along which to insert (0=depth, 1=row, 2=column).
"""


arr = np.array([10, 20, 30 ,40, 50])
print(arr)
new_arr = np.insert(arr, 2, 100, axis=0)
print(new_arr)

arr_2d = np.array([[10, 20, 30], [40, 50, 60]])
print(arr_2d)
new_arr_2d = np.insert(arr_2d, 1, [5, 15, 25], axis=0)
print(new_arr_2d)

arr = np.arange(8).reshape(2, 2, 2)
# arr.shape = (2, 2, 2)
# Insert a new 2x2 "layer" at index 1
new_layer = [[100, 101], [102, 103]]
result = np.insert(arr, 1, new_layer, axis=0)
print(result.shape)  # (3, 2, 2)

new_row = [[200, 201], [202, 203]]
result = np.insert(arr, 0, new_row, axis=1)
print(result.shape)  # (2, 3, 2)

new_col = [[300, 301], [302, 303]]
result = np.insert(arr, 1, new_col, axis=2)
print(result.shape)  # (2, 2, 3)

#  APPEND in NUMPY

"""
SYNTAX - np.append(arr, values, axis=None)
arr: The input array.
values: Values to append to the array.
axis: The axis along which to append. If None (default), both arrays are flattened before appending.
"""

# 1D array
arr = np.array([1, 2, 3])
result = np.append(arr, [4, 5])
print(result)  # Output: [1 2 3 4 5]

# 2D array
arr = np.array([[1, 2], [3, 4]])
result = np.append(arr, [5, 6])
print(result)  # Output: [1 2 3 4 5 6]

arr = np.array([[1, 2], [3, 4]])
new_row = [[5, 6]]
result = np.append(arr, new_row, axis=0)
print(result)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

arr = np.array([[1, 2], [3, 4]])
new_col = [[5], [6]]
result = np.append(arr, new_col, axis=1)
print(result)
# Output:
# [[1 2 5]
#  [3 4 6]]

# 3D array
arr = np.arange(8).reshape(2, 2, 2)
result = np.append(arr, [100, 101])
print(result)
# Output: [  0   1   2   3   4   5   6   7 100 101]

arr = np.arange(8).reshape(2, 2, 2)
new_layer = [[[100, 101], [102, 103]]]
result = np.append(arr, new_layer, axis=0)
print(result.shape)  # Output: (3, 2, 2)

arr = np.arange(8).reshape(2, 2, 2)
new_row = [[[200, 201]], [[202, 203]]]
result = np.append(arr, new_row, axis=1)
print(result.shape)  # Output: (2, 3, 2)

arr = np.arange(8).reshape(2, 2, 2)
new_col = [[[300], [301]], [[302], [303]]]
result = np.append(arr, new_col, axis=2)
print(result.shape)  # Output: (2, 2, 3)







# CONCATENATE in NUMPY
"""
np.concatenate((a1, a2, ...), axis=0)
a1, a2, ...: Arrays to concatenate.
axis: The axis along which to concatenate. Default is 0 (depth).
"""
# 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.concatenate((arr1, arr2))
print(result)  # Output: [1 2 3 4 5 6]

# 2D array
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
result = np.concatenate((a, b), axis=0)
print(result)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

a = np.array([[1, 2], [3, 4]])
b = np.array([[5], [6]])
result = np.concatenate((a, b), axis=1)
print(result)
# Output:
# [[1 2 5]
#  [3 4 6]]

# 3D array
a = np.arange(8).reshape(2, 2, 2)
b = np.array([[[100, 101], [102, 103]]])
result = np.concatenate((a, b), axis=0)
print(result.shape)  # Output: (3, 2, 2)

a = np.arange(8).reshape(2, 2, 2)
b = np.array([[[200, 201]], [[202, 203]]])
result = np.concatenate((a, b), axis=1)
print(result.shape)  # Output: (2, 3, 2)


a = np.arange(8).reshape(2, 2, 2)
b = np.array([[[300], [301]], [[302], [303]]])
result = np.concatenate((a, b), axis=2)
print(result.shape)  # Output: (2, 2, 3)



# DELETE in NUMPY
"""
np.delete(array, index, axis=None)
flattern array
"""
arr = np.array([10, 20, 30, 40, 50])
new_arr = np.delete(arr, 0)
print(new_arr)

#  2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
new_arr_2d = np.delete(arr_2d, 1, axis=0)  # Delete second row
print(new_arr_2d)


# STACK in numpy
"""
vertically
horixontally

vstack() row wise
hstack() column wise
"""

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Vertical stack
result_v = np.vstack((arr1, arr2))
print(result_v)
# [[1 2 3]
#  [4 5 6]]
# Horizontal stack
result_h = np.hstack((arr1, arr2))
print(result_h) # Output: [1 2 3 4 5 6]


# Spliting in numpy
"""
np.split(array, indices_or_sections, axis=0)
array: The input array to split.
indices_or_sections: If an integer, the number of equal sections to split into. If a list, the indices at which to split.
axis: The axis along which to split. Default is 0 (depth).

np.hsplit()
np.vsplit()
"""

arr = np.array([10, 20, 30, 40 ,50, 60])
print(np.split(arr, 2))