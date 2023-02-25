import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

plt.figure(figsize=(5,8), dpi=300)

plt.style.use('ggplot')

barcelona = fifa.loc[fifa['Club'] == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa['Club'] == 'Real Madrid']['Overall']
new_england = fifa.loc[fifa['Club'] == 'New England Revolution']['Overall']

labels = ['FC Barcelona', 'Real Madrid', 'NE Revolution']

#For styling, alot of the stuff you want to do is about the matter of googling. You could read the documentation,
#but sometimes googling can be faster
boxes = plt.boxplot([barcelona, madrid, new_england], labels=labels, patch_artist = True, medianprops={'linewidth':2, 'color':'b'})

#For styling for box n whiskers graphs the annoying part is that some of the styling parameters need to be 
#outside using for loops.
#E.g. if you pass colors into the '.boxplot()' function its gonna give an error as '.boxplot()' does
#not accept the color parameter
#While some the parameters like 'medianprops' can be in the '.boxplot()' function
#Note: 'medianprops' function is to style the median line in the box n whiskers boxes
for box in boxes['boxes']:
    #Set edge color and linewidth
    box.set(color='#4286f4', linewidth=2)

    #Set fill color (the really annoying thing about this is that in order for the 'facecolor' function to work,
    #you need to add the parameter, 'patch_artist = True' into the '.boxplot()' function or else it'll give
    #an error)
    box.set(facecolor='#e0e0e0')

plt.title('FIFA Teams Overall Ratings Comparison')

plt.ylabel('FIFA Team Overall Ratings')
plt.xlabel('FIFA Teams')

plt.savefig('fifa_data_boxnwhiskers.png', dpi=200)

plt.show()