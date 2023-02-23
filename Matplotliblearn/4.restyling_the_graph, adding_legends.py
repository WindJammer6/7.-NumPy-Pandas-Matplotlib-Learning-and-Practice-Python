import matplotlib.pyplot as plt

x = [0,1,2,3,4]
y = [0,2,4,6,8]

#Restyling the line. Many parameters you can put in (refer to documentation) such as label, color, linewidth,
#linestyle, marker, markersize, markeredgecolor, etc...
#Note that for colours you can put single alphabets and hexidecimals as well e.g. 'r' for red, 'y' for yellow and
#'#ababab' for grey

#You can check in the documentation on all the marker (type), linestyle, (line)color supported by matplotlib
plt.plot(x,y, label='y = 2x', color='red', linewidth=2, linestyle='--', marker='.', markersize=10, markeredgecolor='blue')

plt.title('Our First Graph!', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})

plt.xlabel('x axis', fontdict={'fontname':'Arial'})
plt.ylabel('y axis', fontdict={'fontname':'Comic Sans MS'})

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8])  

#Adding a legend
plt.legend()  #shows the y = 2x box in the graph

plt.show()