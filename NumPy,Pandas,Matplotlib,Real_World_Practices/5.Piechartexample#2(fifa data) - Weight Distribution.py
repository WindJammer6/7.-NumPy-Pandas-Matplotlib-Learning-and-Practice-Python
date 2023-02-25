import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

#There are various pie chart styles you can use. Can refer to documentation for it. It may change 
#fonttyple/fontsize of title and labels as well other than changing the colours.

#Documentation: https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html
plt.style.use('ggplot')

#Now in order to work with the weights, we need to remove the 'lbs' word in the string so we can work
#with just the numbers

#There are alot of ways to do this 
#1. '.replace()' the string you dont want with ''
#2. '.sub()' function with '' from the regex expression (re) library
#3. '.strip()' function. If not parameters passed through it will by default remove any leading or trailing
#   spaces (\n) and tabs (\t)  (theres stuff like 'lstrip()' and 'rstrip()' too)
#4. 'removeprefix()' and 'removesuffix()'

#You need to add the int() so that the values you get back (the numbers) are of the integer type
#and not as a string. If you never put the int(), then you will get e.g. '159', which is a string type, not
#int, which may affect your code later

#'type(x)==str' means the data type of the stuff you type in are of a string
fifa['Weight'] = [int(x.replace('lbs', '')) if type(x)==str else x for x in fifa['Weight']]
#fifa['Weight'] = [x.rstrip('lbs') if type(x)==str else x for x in fifa['Weight']] works too

light = fifa[fifa['Weight'] < 125].count()[0]   #adding the fifa.loc works too, but this one also can
light_medium = fifa[(fifa['Weight'] >= 125) & (fifa['Weight'] < 150)].count()[0]
medium = fifa[(fifa['Weight'] >= 150) & (fifa['Weight'] < 175)].count()[0]
medium_heavy = fifa[(fifa['Weight'] >= 175) & (fifa['Weight'] < 200)].count()[0]
heavy = fifa[fifa['Weight'] >= 200].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ['light (<125)', 'light_medium (125<=x<150)', 'medium(150<=x<175)', 'medium_heavy(175<=x<200)', 'heavy(>200)']
explode = [.4,.2,0,0,.4]

#Notice that without the 'pctdistance' the % labels are a little squished to each other.
#So during coding you may meet this kind of weird bugs and you may do a google search to find solutions
#for them (e.g. in this case, google % labels too close for pie chart) and you might get various solutions.

#One such solutions in this case is to use the 'pctdistance', sets the distance of the % labels from the 
#centre of the pie chart. (from 0 to 1, and if you set more than 1 the labels will be outside the pie chart)

#Another way is to use 'explode' which cause the specified segments of the pie chart to split away. The indexing
#of the list will correspond to the labels and weights
plt.pie(weights, labels=labels, autopct='%.2f %%', pctdistance=0.8, explode=explode)

plt.title('Weight distribution of Players in FIFA 2018 (in lbs)')

plt.legend()

plt.savefig('fifa_data_piechart.png', dpi=200)

plt.show()

