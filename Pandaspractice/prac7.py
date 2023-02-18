#Exercise 7: Find the average mileage of each car making company
import pandas as pd

df = pd.read_csv('Automobile_data.csv')

df2 = df.groupby('company').mean()['average-mileage']
print(df2)

#AGGREGATE FUNCTIONS	DESCRIPTION
#count()	   Returns count for each group
#size()	       Returns size for each group
#sum()	       Returns total sum for each group
#mean()	       Returns mean for each group. Same as average()
#average()	   Returns average for each group. Same as mean()
#std()         Returns standard deviation for each group
#var()	       Return var for each group
#sem()	       Standard error of the mean of groups
#describe()	   Returns different statistics
#min()	       Returns minimum value for each group
#max()	       Returns maximum value for each group
#first()	   Returns first value for each group
#last()	       Returns last value for each group
#nth()	       Returns nth value for each group