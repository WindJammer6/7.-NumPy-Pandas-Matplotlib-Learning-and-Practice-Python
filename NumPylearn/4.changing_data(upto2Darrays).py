import numpy as np

#Making a 2D, 2 by 7 array
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])

#Changing element, number 13 to 20
a[1, 5] = 20
print(a)

#Changing rows
a[0, 1:3] = 5

#If you wanna specify what each element will become instead of both becoming the same value
a[0, 1:3] = [6, 7]
print(a)

#Changing columns
a[:, 1] = [1, 2]
print(a)