#How would you index values 11, 12, 16, 17 of this matrix?
#m = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25], [26,27,28,29,30]])
import numpy as np

m = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25], [26,27,28,29,30]])

print(m[2:4, 0:2])


#How would you index values 2, 8, 14, 20 of this matrix?
print(m[[0,1,2,3], [1,2,3,4]])


#How would you index values 4, 5, 24, 25, 29, 30 of this matrix?
print(m[[0,4,5], 3:])