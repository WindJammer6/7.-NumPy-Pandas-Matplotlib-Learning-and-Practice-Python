#Exercise 3: Find the most expensive car company name
import pandas as pd
df = pd.read_csv('Automobile_data.csv')
df = df [['company','price']][df.price==df['price'].max()]
print(df)


#Series can only contain single list with index, whereas dataframe can be made of more than one series 
#or we can say that a dataframe is a collection of series that can be used to analyse the data.

#SERIES COMMANDS          DESCRIPTION
#Series.sum             Return the sum
#Series.min             Return the minimum
#Series.max             Return the maximum     
#Series.idxmin          Return the index of the minimum
#Series.idxmax          Return the index of the maximum
#DataFrame.sum          Return the sum over the requested axis
#DataFrame.min          Return the minimum over the requested axis
#DataFrame.max          Return the maximum over the requested axis
#DataFrame.idxmin       Return the index of the minimum over the requested axis.
#DataFrame.idxmax       Return the index of the maximum over the requested axis.