#How would you index values 11, 12, 16, 17 of this matrix?
#m = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25], [26,27,28,29,30]])
import numpy as np

m = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25], [26,27,28,29,30]])
print(m)

a = (m > 10) & (m < 13)
b = (m > 15) & (m < 18)

print(m[a | b])   #'&' stands for 'and', while '|' stands for 'or'


#How would you index values 2, 8, 14, 20 of this matrix?
print(m[0,1], m[1,2], m[2,3], m[3,4])


#How would you index values 4, 5, 24, 25, 29, 30 of this matrix?
print(m[0:1, 3:5], m[4:6, 3:5])