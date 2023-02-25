import matplotlib.pyplot as plt
import pandas as pd

#These are the 6 most commonly used graphs in matplotlib (matplotlib supports alot more types though (3D ones, errorbar, contour etc...))
#The six most commonly used Plots come under Matplotlib. These are:
#1. Line Plot
#2. Bar Plot
#3. Scatter Plot
#4. Pie Plot
#5. Area Plot
#6. Histogram Plot

#Differences between histogram and bar graph
#1. Histogram refers to a graphical representation; that displays data by way of bars to show the frequency 
#   of numerical data. A bar graph is a pictorial representation of data that uses bars to compare different 
#   categories of data.
#2. A histogram represents the frequency distribution of continuous variables. Conversely, a bar graph is a 
#   diagrammatic comparison of discrete variables.
#3. Histogram presents numerical data whereas bar graph shows categorical data.

fifa = pd.read_csv('fifa_data.csv')

#What are bins?
#A histogram displays numerical data by grouping data into "bins" of equal width.
bins = []
i = 40

while i <= 100:
    bins.append(i)
    i = i + 10
    if i > 100:
        break

#You can google 'colour picker' in google to see the hexidecimals for a certain colour/shade of colour you want
#Link will be attached in the ReadME in my github page
plt.hist(fifa['Overall'], bins=bins, color='#abcdef')   #light blue colour

plt.xticks(bins)

plt.xlabel('Overall rating')
plt.ylabel('Number of Players')
plt.title('Distribution of Player Ratings in FIFA 2018', fontdict={'fontsize':20, 'fontweight':'bold'})

plt.show()