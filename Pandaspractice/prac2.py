#Exercise 2: Clean the dataset and update the CSV file
import pandas as pd

#na_values consider if the inputs for the selected rows are '?' or 'n.a.', they will be considered as 
#na values in python and will be printed as NaN
df = pd.read_csv('Automobile_data.csv', na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
print(df)

df.to_csv('Cleaneddatafromprac2.csv')