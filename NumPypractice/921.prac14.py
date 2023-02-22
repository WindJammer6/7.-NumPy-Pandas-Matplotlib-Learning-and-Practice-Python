#How to reverse the rows of a 2D array?
#Input: arr = np.arange(9).reshape(3,3)
import numpy as np

arr = np.arange(9).reshape(3,3)

print(arr[[2, 1, 0], :])

#Solution (via in reverse steps, no starting and ending index)
print(arr[:, ::-1])
