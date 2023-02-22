#How to extract items that satisfy a given condition from 1D array?
#Input -> arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#Output -> [1, 3, 5, 7, 9]

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[1:10:2])