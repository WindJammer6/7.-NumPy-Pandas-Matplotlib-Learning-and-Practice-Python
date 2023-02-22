#How to swap two columns in a 2d numpy array?
#Swap columns 1 and 2 in the array arr
#Input: arr = np.arange(9).reshape(3,3)
import numpy as np

arr = np.arange(9).reshape(3,3)
arr

# Solution
print(arr[:, [1,0,2]])  #Likewise for to swap rows will be arr[[1,0,2], :]
