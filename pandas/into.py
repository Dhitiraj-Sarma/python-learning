import pandas as pd

# Introduction to Pandas Series and DataFrame
# 1. Creating a DataFrame
# A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

# Output
#     cars  passings
# 0    BMW         3
# 1  Volvo         7
# 2   Ford         2



# 2. Creating a Series
# A Series is a one-dimensional labeled array capable of holding any data type.

# a. From a List

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

# Output
# 0    1
# 1    7
# 2    2
# dtype: int64

# b. Accessing Elements

print(myvar[0])  # Output: 1

# c. Custom Index

a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)

# Output
# x    1
# y    7
# z    2
# dtype: int64


# d. From a Dictionary

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

# day1    420
# day2    380
# day3    390
# dtype: int64

# Series with Selected Index

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

# day1    420
# day2    380
# dtype: int64


# 3. Creating a DataFrame from a Dictionary

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

#    calories  duration
# 0       420        50
# 1       380        40
# 2       390        45