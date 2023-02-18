#Excercise 1: From the given dataset print the first and last five rows
import pandas as pd

df = pd.read_csv('Automobile_data.csv')

#First five rows
print(df.head(5))

##Last five rows
print(df.tail(5))