#Exercise 5: Count total cars per company
import pandas as pd
df = pd.read_csv('Automobile_data.csv')
df2 = df['company'].value_counts()
print(df2)