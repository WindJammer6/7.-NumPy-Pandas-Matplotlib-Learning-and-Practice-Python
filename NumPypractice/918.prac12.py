#How to extract all numbers between a given range from a numpy array?
#Input: a = np.array([2, 6, 1, 9, 10, 3, 27])
#Output: (array([6, 9, 10]),)
import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])

print(a[(a > 5) & (a < 11)])

#Alternate method 1
index = np.where((a >= 5) & (a <= 10))
print(a[index])

#Alternate method 2:
index2 = np.where(np.logical_and(a>=5, a<=10))
print(a[index2])
