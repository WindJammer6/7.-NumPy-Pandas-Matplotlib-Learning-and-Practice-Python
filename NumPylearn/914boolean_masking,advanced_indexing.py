import numpy as np

filedata = np.genfromtxt('data.txt', delimiter = ',')

#Print out filedata array with Boolean Masking (indicates with True or False if the value is larger than
#50)
print(filedata > 50)

#Print out filedata values that have values > 50
a = filedata[filedata > 50]
print(a)

#The reason why this works is because you can actually do indexing with a list in NumPy
b = np.array([1,2,3,4,5,6,7,8,9])
print(b[[1,2,8]])   #This prints out the values in array 'b' of index 1, 2 and 8



#Checks that in every column, and printing a boolean value (True/False), if ANY of the values meet the condition
#e.g. > 50
print(np.any(filedata > 50, axis=0))
print(np.any(filedata > 50, axis=1))   #This would be for the row any value > 50

#Checks that in every column, and printing a boolean value (True/False), if ALL of the values meet the condition
#e.g. > 50
print(np.all(filedata > 50, axis=0))   #Only column 5 (index 4) is True as all of the values is > 50 (196, 766, 999)
print(np.all(filedata > 50, axis=1))   #This would be for the row all value > 50 (False for all 3 rows)



#Putting multiple conditions for Boolean Masking
c = (filedata > 50) & (filedata < 100)
print(c)
d = (~(filedata > 50) & (filedata < 100))   #'~' means do the opposite (put True for all values that are NOT
print(d)                                    #between 50 and 100)