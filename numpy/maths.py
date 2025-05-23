import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr + 5)
print(arr * 2)
print(arr ** 2)

# aggregation functions

arr = np.array([10, 20, 30, 40, 50, 45, 55, 65, 70, 75])

print(arr.sum())  # sum of all elements
print(arr.mean())  # mean of all elements
print(arr.max())  # maximum element
print(arr.min())  # minimum element
print(arr.std())  # standard deviation
print(arr.var())  # variance
print(arr.cumsum())  # cumulative sum
print(arr.cumprod())  # cumulative product