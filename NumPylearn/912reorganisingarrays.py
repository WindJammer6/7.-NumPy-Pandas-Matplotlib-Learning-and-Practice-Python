import numpy as np

before = np.array([[1,2,3,4], [5,6,7,8]])

print(before)

#This array's shape is now (4,2)
print(before.shape)

#We can change its shape to however we want ((8,1), (4,2), (2,2,2) etc...) using '.reshape()'
#As long as the number of values fit. So shapes like ((2,3) or (3,3,3)) won't work and you'll get an error
after = before.reshape(8,1)
after2 = before.reshape(2,2,2)
print(after)
print(after2)

#Vertically stacking matrices
#Note that the arrays you are stacking must share the same column number or else it won't work
#E.g. if v2 is [5,6,7,8,9], then you can't stack it on top of v1
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2,v1,v2])) 

#Horizontally stacking matrices
#Likewise, #Note that the arrays you are stacking must share the same row number or else it won't work
#E.g. if h2 is np.zeros((3,2)), then you can't stack it beside h2
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(np.hstack([h1,h2]))