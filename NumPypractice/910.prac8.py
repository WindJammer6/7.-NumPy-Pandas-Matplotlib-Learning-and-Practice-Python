#How to generate custom sequences in numpy without hardcoding?
#Create the following pattern without hardcoding. Use only numpy functions and the below 
#input array a. (a = np.array([1,2,3]))
#Output: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
import numpy as np

a = np.array([1,2,3])
b= np.repeat(a, 3, axis=0)
c = np.hstack([a, a, a])

d = np.concatenate([b, c], axis=0)
print(d)