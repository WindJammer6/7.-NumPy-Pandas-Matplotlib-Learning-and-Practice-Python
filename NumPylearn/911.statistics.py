import numpy as np

#This falls under Statistics in math, all about min, max, mean, medium  (stuff like sum works too) etc...
stats = np.array([[1,2,3], [4,5,6]])
print(stats)

#Get min of the 2D array (find smallest value in array)
print(np.min(stats))
print(np.min(stats, axis=1))   #You can find min for each row
print(np.min(stats, axis=0))   #You can find min for each column

#Get max of the 2D array (find largest value in array, or row/column by adding the axis parameter 
#(see min example))
print(np.max(stats))
print(np.max(stats, axis=1))
print(np.max(stats, axis=0))

#Get sum of all values in the array
print(np.sum(stats))


