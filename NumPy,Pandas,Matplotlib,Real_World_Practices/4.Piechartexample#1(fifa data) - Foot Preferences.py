import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]   #Putting the [0] helps you just get a single count,
                                                               #(first element) instead of a printing a whole 
                                                               #column of the same numbers

#fifa.loc[fifa['Preferred Foot'].str.contains('Left')] works too
#I think should be ok to use '.groupby()', then use the '.count()' command as well

right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

labels = ['Left Foot', 'Right Foot']
colors = ['r', 'b']

#Note you cannot just put 'plt.pie(fifa['Preferred Foot'])', as you need to pass in actual values for it to work
#BTW, the parameters you pass need to have the 's' behind e.g. 'labels' not 'label' and 'colors', not color' (regardless
#if there is only 1 value or more being passed in)
plt.pie([left, right], labels=labels, colors=colors, autopct='%.2f %%')  #'autopct' allows you to put in the '%' label
                                                                         #into the pie chart. The '%%' puts the '%' sign
                                                                         #else it'll just be the numbers(not very nice looking)

plt.title('Percentage of Preferred Foot of Players in FIFA 2018')

plt.legend()

plt.show()