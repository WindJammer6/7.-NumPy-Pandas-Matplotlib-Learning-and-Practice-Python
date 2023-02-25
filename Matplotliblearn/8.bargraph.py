import matplotlib.pyplot as plt

labels = ['A', 'B', 'C']
values = [1,4,2]

plt.figure(figsize=(6,4))

plt.title('Bar Graph', fontdict={'fontname':'Comic Sans MS', 'fontsize':20, 'fontweight':'bold'})

bars = plt.bar(labels, values)

#You can add some patterns in it using the 'set_hatch()' command. The types of patterns to put can be
#viewed from inside the matplotlib documentation
#First method: This is the normal but can be quite tedious
#bars[0].set_hatch('/')
#bars[1].set_hatch('O')
#bars[2].set_hatch('*')

#Second method:
patterns = ['/', 'O', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))   #The pop() method removes the last element from an array and returns 
                                     #that element. This method changes the length of the array. If you put just
                                     #pop(), the default will to remove the last element from the array and return it
                                     #so in this case if you want first bar to be '/', you need specify 0 in the
                                     #pop(0)

#A bit of the stuff for bar graph above are all the same as line graph
#e.g. fonttype, fontsize, changing ticks, restyling, resize, saving, labelling, etc...
#Though there are some differences

plt.savefig('bargraph.png', dpi=100)

plt.show()