import numpy as np

#Usually we load data using the Pandas library, but you technically could do it with NumPy as well (shown below)

filedata = np.genfromtxt('data.txt', delimiter = ',')
filedata2 = np.genfromtxt('data.txt')
#(delimiter basically tells numpy that this indicates that ',' is a seperator to the next value in the
#file you want to load
#See comparison below:
print(filedata)
print(filedata2)

#Notice that all the data is in floats (as they have '.' at the end of the values)
#To solve that, we redefine the data types from floats (float32/64/...) to ints (int8/16/32...) using the
#'.astype' function
filedata = filedata.astype('int32')
print(filedata)