#How to get the common items between two python numpy arrays?
#Input: a = np.array([1,2,3,2,3,4,3,4,5,6])
#       b = np.array([7,2,10,2,7,4,9,4,9,8])
#Output: array([2, 4])
import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

#'intersect1d()' finds the intersection of two arrays.(only 2)

#To get intersction of 3 or more arrays:
#from functools import reduce
#reduce(np.intersect1d, ([1, 3, 4, 3], [3, 1, 2, 1], [6, 3, 4, 2]))
#array([3])
print(np.intersect1d(a,b))