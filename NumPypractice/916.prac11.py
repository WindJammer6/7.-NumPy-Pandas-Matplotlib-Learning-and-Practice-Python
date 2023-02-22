#How to get the positions where elements of two arrays match?
#Input: a = np.array([1,2,3,2,3,4,3,4,5,6])
#       b = np.array([7,2,10,2,7,4,9,4,9,8])
#Output: (array([1, 3, 5, 7]),)
import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

c = np.c_[a, b]

d = c[c[:, 0] == c[:, 1]]

e = d[:, 0]

print(np.where(a == b))

