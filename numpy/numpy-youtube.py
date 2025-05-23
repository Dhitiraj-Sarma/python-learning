import numpy as np

#  How to check shape of a array

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d.shape) # (2, 3)

# How to check size of a array (total number of elements of an array)

print(arr_2d.size) # 6

# How to check number of dimensions

print(arr_2d.ndim) # 2

#  How to check data-type

print(arr_2d.dtype) # int64

arr = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])
print(arr)
print(arr.ndim)
print(arr.shape)

# changing type of a array

arr = np.array([1.2, 1.3, 2.5, 4.5])
int_arr = arr.astype(int)

print(int_arr) # [1 1 2 4]
print(int_arr.dtype) # int64