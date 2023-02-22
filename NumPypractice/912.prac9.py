#How to get the common items between two python numpy arrays?
#Input: a = np.array([1,2,3,2,3,4,3,4,5,6])
#       b = np.array([7,2,10,2,7,4,9,4,9,8])
#Output: array([2, 4])
import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

c = np.c_[a, b]
print(c)

d = c[c[:, 0] == c[:, 1]]
print(d)