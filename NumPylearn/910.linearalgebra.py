import numpy as np

#This falls under Mathematical Matrices (Linear Algebra), and matrix addition/subtraction/multiplication in
#'O' Level. Important note that Matrices cannot undergo division. 

#If forget the rules alr can refresh your memory through googling
a = np.ones((2,3))
b = np.full((3,2), 2)

print(a)
print(b)

#Now, you cannot simply just do this, it will give an error
#print(a * b)

#Need to use special command to multiply 2 matrices
print(np.matmul(a,b))

#Find determinant of matrices (basically something you get from doing some math with the values in a matrix)
#and that the determinant is always 1 for identity matrices
c = np.identity(3)
np.linalg.det(c)  #'.linalg' means linear algebra and '.det' means determinant


#Link for Linear Algebra and Matrices reference documentation: https://numpy.org/doc/stable/reference/routines.linalg.html
#Determinants
#Trace
#Singular Vector Decomposition
#Eigenvalues
#Matrix Norm
#Inverse
#Etc...