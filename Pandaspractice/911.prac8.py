#Exercise 8: Sort all cars by Price column
import pandas as pd

df = pd.read_csv('Automobile_data.csv')

df2 = df.sort_values('price', ascending=False)
print(df2)