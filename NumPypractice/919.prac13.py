#How to swap two columns in a 2d numpy array?
#Swap columns 1 and 2 in the array arr
#Input: arr = np.arange(9).reshape(3,3)
import numpy as np

arr = np.arange(9).reshape(3,3)

a = arr[:, 0].copy()
b = arr[:, 1].copy()

arr[:, 0] = b
arr[:, 1] = a

print(arr)