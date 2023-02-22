#How to remove from one array those items that exist in another?
#Input: a = np.array([1,2,3,4,5])
#       b = np.array([5,6,7,8,9])
#Output: array([1,2,3,4])
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

c = np.intersect1d(a, b)

d = np.delete(a, c, axis=0)

#/////////////////////// incomplete answer