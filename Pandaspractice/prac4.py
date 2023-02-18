#Exercise 4: Print All Toyota Cars details
import pandas as pd
import re

df = pd.read_csv('Automobile_data.csv')

a = df.loc[df['company'].str.contains('toyota', flags=re.I, regex=True)]
print(a)

