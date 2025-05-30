import numpy as np
"""
np.insert(array, index, value, axis=None)
array - original array
index -
value -
axis - 0 - row wise
		1 - column wise
"""


arr = np.array([10, 20, 30 ,40, 50])
print(arr)
new_arr = np.insert(arr, 2, 100, axis=0)
print(new_arr)

arr_2d = np.array([[10, 20, 30], [40, 50, 60]])
print(arr_2d)
new_arr_2d = np.insert(arr_2d, 1, [5, 15, 25], axis=0)
print(new_arr_2d)