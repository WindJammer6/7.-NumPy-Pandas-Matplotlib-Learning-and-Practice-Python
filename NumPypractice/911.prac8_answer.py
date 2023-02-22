#How to generate custom sequences in numpy without hardcoding?
#Create the following pattern without hardcoding. Use only numpy functions and the below 
#input array a. (a = np.array([1,2,3]))
#Output: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
import numpy as np

a = np.array([1,2,3])

#'tile()' constructs an array by repeating A the number of times given by reps.
#e.g. a = np.array([0, 1, 2])
#     np.tile(a, 2)
#     output: array([0, 1, 2, 0, 1, 2])
#e.g. np.tile(a, (2, 1, 2))
#     output: array([[[0, 1, 2, 0, 1, 2]],
#            [[0, 1, 2, 0, 1, 2]]])
print(np.r_[np.repeat(a, 3), np.tile(a, 3)])