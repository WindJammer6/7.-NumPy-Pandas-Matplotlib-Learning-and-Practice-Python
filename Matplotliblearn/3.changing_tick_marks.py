import matplotlib.pyplot as plt

x = [0,1,2,3,4]
y = [0,2,4,6,8]

plt.plot(x,y)

plt.title('Our First Graph!', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})

plt.xlabel('x axis', fontdict={'fontname':'Arial'})
plt.ylabel('y axis', fontdict={'fontname':'Comic Sans MS'})

#Adding tick marks at the x and y axis (basically the number labels at the x and y axis)
#e.g. you want those points to be integers so you change them to ints (cuz default may have decimals)

#Note that the graph will auto resize for you depending of the numbers you put as the ticks
#e.g. plt.xticks([0,1,2,3,4, 1000]) you will get a weird looking graph as it stretches out the x axis alot to plot
#in the tick for number 1000
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,7,7.5,8])  #note that even if you didnt put the numbers of equal intervals, matplotlib will
                               #still place those odd numbers (7 and 7.5) at the right spots in relation to the
                               #other numbers
plt.show()