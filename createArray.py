import numpy as np

# ndarray
# 0D Array
arr0 = np.array(100)
print(type(arr0))
print(arr0)
# so, if I want to find the diamentions of our array
# there is property / attribute in python *ndim*
print(arr0.ndim)

# 1D Array
arr1 = np.array([10,20,30]) # data in List form
print(type(arr1))
print(arr1)
print(arr1.ndim)

# 2D Array
# for 2D array we have to give sublist means List within a List
arr2 = np.array([[10,20,30],[40,50,60]])
print(arr2)
print(arr2.ndim)

# 3D Array
# It is a multiple 2D arrays means 3D array
# 
arr3 = np.array([[[10,20,30],[40,50,60],
                  [70,80,90],[100,110,120]]])
print(arr3)
print(arr3.ndim)
