import matplotlib.pyplot as plt

x = [1,2,3]
y = [2,4,6]

plt.plot(x,y)

#Adding a title for the graph, and changing the font type, font size and font weight of the title
plt.title('Our First Graph!', fontdict={'fontname':'Comic Sans MS', 'fontsize':20, 'fontweight':'bold'})

#Adding a label for the x and y axis
plt.xlabel('x axis', fontdict={'fontname':'Arial'})  #Arial is the default font type so this technically does nothing
plt.ylabel('y axis', fontdict={'fontname':'Comic Sans MS'})

plt.show()