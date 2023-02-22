#How to stack two arrays vertically?
#Stack arrays a and b vertically
#Input: a = np.arange(10).reshape(2,-1)
#       b = np.repeat(1, 10).reshape(2,-1)
import numpy as np

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

print(np.vstack([a,b]))

#Alternate method 1
print(np.concatenate([a, b], axis=0))

#Alternate method 2
print(np.r_[a, b])