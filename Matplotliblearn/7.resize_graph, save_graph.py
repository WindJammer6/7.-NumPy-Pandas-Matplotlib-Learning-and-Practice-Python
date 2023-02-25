import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4]
y = [0,2,4,6,8]

#Resize graph
#'figsize' sorts of sets the ratio of your graph (x to y)(or dimensions)
#'dpi' means something like pixels per inch, which specifies how big your graph is (300 in recommended),
#smaller number will give smaller graphs. This will give (if figsize is (5,3), 1500 pixels x 900 pixels)

#Another important note, this resizing command must be at the top of the program and before the '.plot()'
#commands or else it will cause funny bugs (e.g. open 2 windows and title being in the (wrong) empty window
plt.figure(figsize=(5,3), dpi=300)

plt.plot(x,y, 'r^-', label='y = 2x')

x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:6], x2[:6]**2, 'b^-', label='y = x^2')    
plt.plot(x2[5:], x2[5:]**2, 'b^--', label='y = x^2')   

plt.title('Our First Graph!', fontdict={'fontname':'Comic Sans MS', 'fontsize':20, 'fontweight':'bold'})

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.xticks([0,1,2,3,4])

plt.legend()

#Saving the graph
#You can also specify the pixels for your graph that you want to save (while the one you see
#in the code may have a different pixel size)
plt.savefig('linegraph.png', dpi=100)

plt.show()