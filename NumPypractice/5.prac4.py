#How to replace items that satisfy a condition with another value in numpy array?
#Replace all odd numbers in arr with -1 without changing arr

#Input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#Output: array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr2 = arr.copy()

arr2[arr2 % 2 == 1] = -1

print(arr2)
print(arr)



