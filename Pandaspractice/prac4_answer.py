#Exercise 4: Print All Toyota Cars details
import pandas as pd
df = pd.read_csv('Automobile_data.csv')
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
print(car_Manufacturers)
print(toyotaDf)

#The returned GroupBy object (it is a DICTIONARY!!) is nothing but a dictionary where keys are the unique groups in 
#which records are split and values are the columns of each group which are not mentioned in groupby. 

#Certainly, GroupBy object holds contents of entire DataFrame but in more structured form. If you print out the groupby() object you 
#will get a weird looking output: 'pandas.core.groupby.generic.DataFrameGroupBy'

#However, with this groupby object, you can add many interesting commands to it to filter data.

#The code below assumed you have a variable already storing a groupby() object e.g. a = df.groupby['']

#GROUPBY COMMANDS                    DESCRIPTION
#ngroups()          To look at how many unique groups can be formed in the column.
#size()             To look at number of rows in each group of GroupBy object. Includes null values.
#count()            Quite similar to size, but it does not count null values.
#first()            Gets first row
#last()             Gets last row
#nth(), nth(-1)     A specific row (e.g. .nth(3) gets you the fourth row) and nth(-1) gets you last row


