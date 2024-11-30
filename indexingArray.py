import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,])

print(arr)

#Access Array Elements
#You can access an array element by referring to its index number.
#The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

print(arr[0])
print(arr[3])
print(arr[3] - arr[2])

#Access 2-D Arrays
#To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
#Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.

arr1 = np.array([[10,20,30,40,50],[60,70,80,90,100]])

print(arr1)
print('2nd element on 1st row:', arr1[0,1])
print('3nd element on 2st row:',arr1[1,2])

#Access 3-D Arrays
#To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.

arr2 = np.array([[[100,200,300],[300,400,500]],
                [[500,600,700],[700,800,900]]])
print(arr2)
print(arr2[0,1,2]) #Access the third element of the second array of the first array


#Negative Indexing
#Use negative indexing to access an array from the end.
arr3 = np.array([[11,12,13,14,15],[16,17,18,19,20]])
print(arr3)
print('last element from 2nd dim:', arr3[1,-1])
