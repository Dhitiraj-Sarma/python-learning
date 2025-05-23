import numpy as np

"""
reshape(rows, columns) specify new shape
if dimentions match
it return a view not a copy
"""

arr = np.array([1, 2, 3, 4, 5, 6])
reshape_arr = arr.reshape(3, 2)
print(reshape_arr) # [[1 2] [3 4] [5 6]]

"""
ravel() -> view
flatten() -> copy
"""

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_2d.ravel()) # [1 2 3 4 5 6]
print(arr_2d.flatten()) # [1 2 3 4 5 6]
print(arr_3d.ravel()) # [1 2 3 4 5 6 7 8]