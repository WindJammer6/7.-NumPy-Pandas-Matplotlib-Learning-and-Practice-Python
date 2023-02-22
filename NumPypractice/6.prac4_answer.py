#How to replace items that satisfy a condition with another value in numpy array?
#Replace all odd numbers in arr with -1 without changing arr

#Input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#Output: array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])

import numpy as np

arr = np.arange(10)  

out = np.where(arr % 2 == 1, -1, arr)

print(arr)
print(out)

#The 'arange()' function allows you to generate an array of numbers (ints/floats)
#'.arange(start, stop, step)' START indicates the number you want to start
#in the array while STOP indicates till which number you want to stop generating
#numbers. STEP tells numpy if you want to skip any values.

#e.g. np.arange(3,7,2)
#output: array([3, 5])

#e.g. np.arange(3,7)
#output: array([3,4,5,6])


#The '.where()' function takes in the parameters, (condition, [x, y, ], (if condition not fulfilled what happens))
#See the example:
#e.g. (input: a = np.arange(10))
#np.where(a < 5, a, 10*a)
#output: array([ 0,  1,  2,  3,  4, 50, 60, 70, 80, 90])

#Prints values if values in a are less than 5, else the rest multiply by 10 and print them out too