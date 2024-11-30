import numpy as np

# ndarray / The array object in NumPy is called ndarray.
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr)) #type(): This built-in Python function tells us the type of the object passed to it.

print(   )
# 0D Array / 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
arr0 = np.array(100)
print(type(arr0))
print(arr0)
# so, if I want to find the diamentions of our array
# there is property / attribute in python *ndim*
print(arr0.ndim) # A dimension in arrays is one level of array depth (nested arrays).

# 1D Array / An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
arr1 = np.array([10,20,30]) # data in List form
print(type(arr1))
print(arr1)
print(arr1.ndim)

# 2D Array / An array that has 1-D arrays as its elements is called a 2-D array.
# for 2D array we have to give sublist means List within a List
arr2 = np.array([[10,20,30],[40,50,60]])
print(arr2)
print(type(arr2))
print(arr2.ndim)

# 3D Array / An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# It is a multiple 2D arrays means 3D array
# 
arr3 = np.array([[[10,20,30],[40,50,60],
                  [70,80,90],[100,110,120]]])
print(arr3)
print(type(arr3))
print(arr3.ndim)


#Higher Dimensional Arrays
#When the array is created, you can define the number of dimensions by using the ndmin argument.

arr4 = np.array([100,200,300,400], ndmin=3)
print(arr4)
print('number of diamentions : ', arr4.ndim)
