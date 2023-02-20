#Initialise this array pattern (try your best not to hardcode)
#[[1. 1. 1. 1. 1.]
# [1. 0. 0. 0. 1.]
# [1. 0. 9. 0. 1.]
# [1. 0. 0. 0. 1.]
# [1. 1. 1. 1. 1.]]
import numpy as np

a = np.ones((5,5))
print(a)

b = np.zeros((3,3))
b[1,1] = 9
print(b)

a[1:4,1:4] = b
print(a)


#Be careful when copying numpy arrays!!!
#e.g. you want to copy array variable 'c' into another variable 'd'
c = np.array([1,2,3])
print(c)

#d = c
d = c.copy()

d[0] = 100
print(d)
print(c)    

#Notice even though you only want to change first element in array d to 100, you somehow accidentaly
#changed array c's first element to 100 as well. This is because by saying d = c, you are telling numpy
#that you want array d to be the same as array c (like both are pointing to the same array in memory.)

#To prevent this, you need to use '.copy()' function to make a copy of array c and then storing that in
#array d
