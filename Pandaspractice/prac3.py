#Exercise 3: Find the most expensive car company name
import pandas as pd

df = pd.read_csv('Automobile_data.csv')

a = df.sort_values(['price'], ascending=False)
a = a.drop(columns=['Unnamed: 0'])

d2 = a.reset_index(drop=True)

#Most expensive car company
d3 = d2[['company', 'price']]
print(d3.head(1))

d4 = d3.set_index('company')

print(d4.head(1))



