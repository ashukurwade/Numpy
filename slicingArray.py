# #Slicing arrays
# # Slicing in python means taking elements from one given index to another given index.
# # We pass slice instead of index like this: [start:end].
# # We can also define the step, like this: [start:end:step].
# # If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

import numpy as np

arr = np.array([100,200,300,400,500,600,700,800,900])
print(arr)

# Slice elements from index 1 to index 5 from the following array

print(arr[1:5]) #-> 200,300,400,500

# Note: The result includes the start index, but excludes the end index.

# Slice elements from index 4 to the end of the array
print(arr[4:])

#Slice elements from the beginning to index 4 (not included)
print(arr[:4])


## Negative Slicing ##

# Use the minus operator to refer to an index from the end:

#Slice from the index 3 from the end to index 1 from the end
print(arr[-3:-1])


## STEP ##

# Use the step value to determine the step of the slicing:

# Return every other element from index 1 to index 5
print(arr[1:5:2])


# Return every other element from the entire array
print(arr[::2])

## Slicing 2-D Arrays ##

arr1 = np.array([[10,20,30,40,50],[60,70,80,90,100]])
print(arr1)

# From the second element, slice elements from index 1 to index 4 (not included)
print(arr1[1,1:4])
# Note: Remember that second element has index 1

# From both elements, return index 2
print(arr1[0:2,2])

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array
print(arr1[0:2,1:4])


