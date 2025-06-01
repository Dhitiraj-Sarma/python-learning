import numpy as np

# Handling Missing Values in NumPy
"""
Missing values in NumPy arrays are typically represented by np.nan (Not a Number) for floating-point arrays. 
NumPy provides several functions to detect, remove, or replace these missing values.



"""

# Detecting Missing Values

arr = np.array([1, 2, np.nan, 4])
mask = np.isnan(arr)
print(mask)  # Output: [False False  True False]


#  Replacing Missing Values
# Use np.nan_to_num() to replace np.nan with a specified value (default is 0).

arr = np.array([1, 2, np.nan, 4])
filled_arr = np.nan_to_num(arr, nan=0)
print(filled_arr)  # Output: [1. 2. 0. 4.]


# Removing Missing Values
# Use boolean indexing to filter out np.nan values.

arr = np.array([1, 2, np.nan, 4])
clean_arr = arr[~np.isnan(arr)]
print(clean_arr)  # Output: [1. 2. 4.]

# You can also use np.where() for custom replacement:
arr = np.array([1, 2, np.nan, 4])
arr = np.where(np.isnan(arr), -1, arr)
print(arr)  # Output: [ 1.  2. -1.  4.]


#  Aggregation Functions Ignoring NaN
# NumPy provides special functions that ignore np.nan values:

# np.nansum(arr): Sum, ignoring NaN.
# np.nanmean(arr): Mean, ignoring NaN.
# np.nanmin(arr), np.nanmax(arr): Min/Max, ignoring NaN.

arr = np.array([1, 2, np.nan, 4])
print(np.nansum(arr))   # Output: 7.0
print(np.nanmean(arr))  # Output: 2.333...


# . Handling Missing Values in 2D Arrays
# All the above methods work with 2D arrays as well, using axis arguments if needed.

arr2d = np.array([[1, np.nan], [3, 4]])
print(np.isnan(arr2d))
# Output:
# [[False  True]
#  [False False]]


# np.isinf(array)

arr = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(np.isinf(arr))

# replace inf

clean_arr = np.nan_to_num(arr, posinf=1000, neginf=1000)
print(clean_arr)