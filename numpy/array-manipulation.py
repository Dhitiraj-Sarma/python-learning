import numpy as np

# NumPy Copy and View of Array

"""
Definition: The main difference between copy and view is that the copy 
is the new array whereas the view is the view of the original array. 
In other words, it can be said that the copy is physically stored at 
another location and the view has the same memory location as the original array.
"""

# View  (Shallow Copies) of Array in NumPy
# A view does not own its data; it simply provides an alternate “window” onto the same buffer. Any in-place change to either the original or the view is reflected in the other.

# creating array 
arr = np.array([2, 4, 6, 8, 10]) 
# creating view 
v = arr.view() 
# both arr and v have different id 
print("id of arr", id(arr)) # 2135584237072
print("id of v", id(v)) # 2135588402352
# changing original array 
# will effect view 
arr[0] = 12
# printing array and view 
print("original array- ", arr) # [12  4  6  8 10]
print("view- ", v) # [12  4  6  8 10]

# changing the view array
v[0] = 99
print("original array- ", arr) # [99  4  6  8 10]
print("view- ", v) # [99  4  6  8 10]