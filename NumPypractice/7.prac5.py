#How to reshape an array?
#Convert a 1D array to a 2D array with 2 rows
#Input: a = np.arange(10)

import numpy as np

a = np.arange(10)

b = a.reshape(2,5)

#OR put column = -1, which tells numpy to automatically decide the number 
#of columns

print(b)