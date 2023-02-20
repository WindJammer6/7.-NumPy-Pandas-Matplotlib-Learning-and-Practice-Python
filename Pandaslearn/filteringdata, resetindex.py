import pandas as pd

poke_dataset_csv = pd.read_csv('pokemon_data.csv')

#Filtering out data
#& is the command for 'and', | is the command for 'or'
#Using the commands 'and' and 'or' does not work
new_data = poke_dataset_csv.loc[(poke_dataset_csv['Type 1'] == 'Grass') & (poke_dataset_csv['Type 2'] == 'Poison')]
print(new_data)

new_data2 = poke_dataset_csv.loc[(poke_dataset_csv['Type 1'] == 'Grass') & (poke_dataset_csv['Type 2'] == 'Poison') & (poke_dataset_csv['HP'] > 70)]
print(new_data2)

new_data2.to_csv('filtered_pokemon_data.csv')


#Reset index of new dataset, since for new datasets their indexes are of the
#old datasets'
new_data3 = new_data2.reset_index(drop=True)  #drop=True means to drop the old indexes so only the new indexes remain
print(new_data3)