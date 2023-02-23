import matplotlib.pyplot as plt

x = [0,1,2,3,4]
y = [0,2,4,6,8]

#Normal way to restyle your graph
#plt.plot(x,y, label='y = 2x', color='red', 'linestyle='--', marker='^')

#Shortcut (shorthand notation) to restyle your graph 'fmt = '[linecolor][marker][linestyle]
#This does the exact same thing as the code above
plt.plot(x,y, 'r^--', label='y = 2x')

plt.title('Our First Graph!', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8])  

plt.legend()

plt.show()