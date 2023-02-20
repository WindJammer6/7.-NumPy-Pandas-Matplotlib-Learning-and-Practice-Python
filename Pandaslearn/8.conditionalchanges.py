import pandas as pd

poke_dataset_csv = pd.read_csv('pokemon_data.csv')
updated_poke_dataset_csv = pd.read_csv('updated_pokemon_data.csv')

#How to convert all the boxes in column 'Type 1' with the word, 'Fire' to 'Flamer' instead
poke_dataset_csv.loc[poke_dataset_csv['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
print(poke_dataset_csv)

#To change 'Flamer' back to 'Fire'
poke_dataset_csv.loc[poke_dataset_csv['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'
print(poke_dataset_csv)

#To make all 'Fire' type pokemon's 'Legendary' status be True
#Show that you can use condition from 1 column to set the parameter of another column  and edit the other column
poke_dataset_csv.loc[poke_dataset_csv['Type 1'] == 'Fire', 'Legendary'] = True
print(poke_dataset_csv)


#If 'Total' column has value higher than 500, set values for those rows(pokemon) for the 'Generation' column to 'Test 1' and
#'Legendary' column to 'Test 2'
updated_poke_dataset_csv.loc[updated_poke_dataset_csv['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']
print(updated_poke_dataset_csv)

#Setting Speed column to 'Test 3' if 'Total' column value higher than 500
updated_poke_dataset_csv.loc[updated_poke_dataset_csv['Total'] > 500, ['Speed']] = 'Test 3'
print(updated_poke_dataset_csv)
