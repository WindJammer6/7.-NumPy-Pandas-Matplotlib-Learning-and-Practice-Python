import matplotlib.pyplot as plt

#Plotting a graph with '.plot(x,y)'. Usually takes in 1D arrays representing the x and y coordinates in the
#x and y axis. 
#plot(x, y)        # plot x and y using default line style and color
#plot(x, y, 'bo')  # plot x and y using blue circle markers
#plot(y)           # plot y using x as index array 0..N-1
#plot(y, 'r+')     # ditto, but with red plusses
#If x and/or y are 2D arrays a separate data set will be drawn for every column. If both x and y are 2D, they
#must have the same shape. If only one of them is 2D with shape (N, m) the other must have length N and will 
#be used for every data set m.
x = [1,2,3]
y = [2,4,6]

plt.plot(x,y)

#Adding a title for the graph
plt.title('Our First Graph!')

#Adding a label for the x and y axis
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()