import numpy as np

#Printing 1D numpy arrays
a = np.array([1,2,3])
print(a)

#Printing 2D numpy array with floats as elements (list within a list)
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)

#Printing 3D arrays (list within a list within a list)
d = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(d)

#Get dimension
print(a.ndim)
print(b.ndim)
print(d.ndim)

#Get shape (like length for 1D, rows and columns for 2D, length, width and height for 3D)
print(a.shape)
print(b.shape)
print(d.shape)

#////////////////////////////////////////////

#Get type (dtype stands for data type), will show either int8, int16 (bits = 16), int32 (bits = 32), basically how many
#bits(binary values) each element is programmed to have in the numpy array 
#(e.g. int 5 in binary int16 is equal to 2 bytes, or 16 bits (1 byte = 8 bits), which looks like this:
#00000000 00000101)
#By default if not specified, numpy elements will be int32, or 32 bits

#Floats are usually larger in bit/byte size compared to integers
print(a.dtype)
print(b.dtype)

c = np.array([1,2,3,4], dtype='int16')
print(c.dtype)

#Get itemsize (itemsize stands for number of bytes)
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

#Get size (gets total number of elements in the numpy array)
print(a.size)
print(c.size)

#Get total itemsize (total bytes in the numpy array)
print(a.size * a.itemsize)
print(a.nbytes)  #.nbytes work too