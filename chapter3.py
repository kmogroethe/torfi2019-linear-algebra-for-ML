#!/usr/bin/env python

import numpy as np

h = "############################################################"

#Define a number
a = 10
print('Type, before converting: ', type(a))
print(a)

#Change the type to float with NumPy
b = np.float64(a)
print('Type, after converting: ', type(b))
print(b)

#Change the type to float with NumPy
c = float(a)
print('Type, after converting: ', type(c))
print(c)

print(h)

# Define a Python list
a = [1,2,1.3]
print ('Type "a": ', type(a))

# Turn python list into a numpy array of type np.int32
b = np.int32(a)
print('Array "b": ', b)
print('Type array "b": ', type(b))
print('Array "b" data type: ', b.dtype)

#Turn python list into a numpy array of type np.float32 (= to python.float)
c = np.float32(a)
print('Array "c": ', c)
print('Type array "c": ', type(c))
print('Array "c" data type: ', c.dtype)

print(h)

#change type of numpy array:
a = [1, 2, 4]
print('Type "a": ', type(a))
b=np.int32(a)
print('Array "b": ', b)
print('Type array "b": ', type(b))
c= b.astype(np.float32)
print('Array "c" ', c)
print('Type array "c": ', type(c))

print(h)

#Create an array from a list
mylist = [1,2,3,4]
numpy_array = np.array(mylist)
print('Array: ', numpy_array)

numpy_array = np.array([1,2,3,4])
print('Array: ', numpy_array)

print(h)

row1 = [2,4,6,8]
row2 = [1,3,5,7]
numpy_array = np.array([row1, row2])
print('Array: ', numpy_array)
print('Shape: ', numpy_array.shape)
