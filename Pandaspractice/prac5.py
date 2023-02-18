#Exercise 5: Count total cars per company
import pandas as pd

df = pd.read_csv('Automobile_data.csv')

df['count'] = 1

df2 = df.groupby(['company']).count()['count']
print(df2)
