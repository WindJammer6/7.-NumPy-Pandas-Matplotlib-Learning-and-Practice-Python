import numpy as np

a = np.array([1,2,3,4])
print(a)

#Addition of the elements
print(a + 2)

#Subtraction of the elements
print(a - 2)

#Multiplication of the elements
print(a * 2)

#Squaring of the elements
print(a ** 2)  #This means (a * 2^2)

#Division of the elements
print(a / 2)

#Add/Subtract/Multiply/Divide 2 arrays together
b = np.array([1,0,1,0])
print(a + b)

#Trigonometry-ing the elements
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))

print(np.log(a))
print(np.log10(a))
print(np.log2(a))