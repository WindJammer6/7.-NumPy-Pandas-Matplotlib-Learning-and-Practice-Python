import numpy as np

#Making a 2D, 2 by 7 array
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)
print(a.shape)

#Get a specific element, e.g. 13 with [r, c] (r is row index, c is column index)
#We visualise it as a table, so number 13 is in row 1 (as python always index first row as 0), and column
#5 (as python similarly always index first column as 0)
print(a[1,5])
print(a[1,-2])  #this works too. The -2 will index the elements in reverse order. e.g. 14 will be index -1, and 13
                #13 will be index -2

#Get a specific row using the [r, c] function too
print(a[0, :])     #index 0 represents row zero, the empty ':' represents all columns. '0:3' represents take
print(a[0, 0:3])   #index 0 to 2 columns

#Get a specific column using the [r, c] function too
print(a[:, 2])

#Getting a little fancy with this trick to print out even numbers in row 0
#[startindex:endindex:stepsize]
print(a[0, 1:6:2])
print(a[0, 1:-1:2])  #works similarly as the code above


#Making a 3D array, 2 by 2 by 2 array
b = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(b)

#Get a specific element in the 3D array 
#(work outside in, from [index_list_outside:index_list_inside:index_list_inside_of_list_inside])
print(a[0:1:1])   #to get number 4

