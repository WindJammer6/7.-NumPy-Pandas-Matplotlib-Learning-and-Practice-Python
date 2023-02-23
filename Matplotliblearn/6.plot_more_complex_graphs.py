import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4]
y = [0,2,4,6,8]

#First graph
plt.plot(x,y, 'r^-', label='y = 2x')

#Second graph
x2 = np.arange(0,4.5,0.5)
#plt.plot(x2, x2**2, 'b^-', label='y = x^2')

#You could do something cool with the second graph like making the first half of the graph a solid line,
#then second half as dotted lines
plt.plot(x2[:6], x2[:6]**2, 'b^-', label='y = x^2')    #(up till index 6)
plt.plot(x2[5:], x2[5:]**2, 'b^--')   #made the indexing overlap abit so the graph looks better (index 5 onwards)

plt.title('Our First Graph!', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.xticks([0,1,2,3,4])
#plt.yticks([0,2,4,6,8])  #Commented this out so that the ticks for y will stretch to all the way to top of y axis

plt.legend()

plt.show()