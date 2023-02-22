#How to stack two arrays vertically?
#Stack arrays a and b vertically
#Input: a = np.arange(10).reshape(2,-1)
#       b = np.repeat(1, 10).reshape(2,-1)
import numpy as np

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

print(np.hstack([a, b]))

#Alternate method 1
#numpy.concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")
#Join a sequence of arrays along the specified axis
print(np.concatenate([a, b], axis=1))

#Alternate method 2
#Translates slice objects to concatenation along the second axis (axis=1)
#e.g. np.c_[np.array([1,2,3]), np.array([4,5,6])]
#     output: array([[1, 4],
#                    [2, 5],
#                    [3, 6]])
#e.g. np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]
#     output: array([[1, 2, 3, 0, 0, 4, 5, 6]])
print(np.c_[a, b])

