import numpy as np

#Making an all 0s matrix
a = np.zeros(5)
print(a)  #1D array

b = np.zeros((2,2))
print(b)  #2D array

c = np.zeros(((2,2,2)))
print(c)  #3D array

#Making an all 1s matrix
d = np.ones((4,2,2), dtype="int32")
print(d)

#Making an all of any other number. '.full()' function takes 2 parameters, the shape, and the number 
#you want to fill the elements with
e = np.full((2,2), 99, dtype="float32")
print(e)

#Making an all of any other number using 'full_like()', which allows you to take in other array variables as its parameter
#if you put 2D array 'f' in shape parameter it will create a new array with the shape of array 'f', but only takes the shape,
#without its elements in it

#Creating a temporary 2D array
f = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
g = np.full_like(f, 4)  #g = np.full(f.shape, 4) works similarly too
print(g)

#Making a random decimal numbers matrix
h = np.random.rand(4,2)
i = np.random.rand(4,2,3)
print(h)
print(i)

j = np.random.random_sample(f.shape)  #need use 'random_sample' command in order to take in array variables
print(j)

#Making a random integer numbers matrix
k = np.random.randint(7, size=(3,3))     #first parameter sets range of the random integers. So 7 means range from 0 to 7.
                                         #second parameter sets the shape, but the command is size here dk why but it works

l = np.random.randint(4,7, size=(3,3))   #sets range of the random integers to 4(inclusive) to 7(exclusive)
m = np.random.randint(-4,8, size=(3,3))  #negative numbers as random integers works too
print(k)
print(l)
print(m)

#Making the identity matrix (An identity matrix is a square matrix in which all the elements of principal 
#diagonals are one, and all other elements are zeros)
n = np.identity(5)
print(n)

#Repeating an array ('.repeat' has 3 parameters, the array, number of times to repeat, around which axis)
arr = np.array([[1,2,3]])       #Need to ensure this is a 2D array first to duplicate this row 
r1 = np.repeat(arr, 3, axis=0)  #into all 3 columns via axis=0
print(r1)