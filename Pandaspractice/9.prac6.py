#Exercise 6: Find each company’s highest price car
import pandas as pd

df = pd.read_csv('Automobile_data.csv')

df2 = df.groupby('company').max()['price']
print(df2)