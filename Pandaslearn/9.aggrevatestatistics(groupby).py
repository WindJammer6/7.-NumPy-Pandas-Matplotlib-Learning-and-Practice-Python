import pandas as pd

updated_poke_dataset_csv = pd.read_csv('updated_pokemon_data.csv')

#Most used groupby functions are .mean(), .sum(), .count()
a = updated_poke_dataset_csv.groupby(['Type 1']).mean().sort_values('Total', ascending=False)
print(a)

b = updated_poke_dataset_csv.groupby(['Type 1']).sum()
print(b)

#Count only counts those boxes that are filled with a value. Hence for 'Type 2' column some of the boxes are
#blank hence they arent counter resulting in the count for 'Type 2' being different from the rest
c =  updated_poke_dataset_csv.groupby(['Type 1']).count()
print(c)

#Creating a 'count' column
updated_poke_dataset_csv['count'] = 1

#To see just the newly created 'count' column
d = updated_poke_dataset_csv.groupby(['Type 1']).count()['count']
print(d)

#Can filter out even further by adding multiple parameters in the groupby function
e = updated_poke_dataset_csv.groupby(['Type 1', 'Type 2']).count()['count']
print(e)