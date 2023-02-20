import pandas as pd

poke_dataset_csv = pd.read_csv('pokemon_data.csv')

poke_dataset_csv['Total'] = poke_dataset_csv.iloc[:, 4:10].sum(axis=1)  

columns = list(poke_dataset_csv.columns)
poke_dataset_csv = poke_dataset_csv[columns[0:4] + [columns[-1]] + columns[4:12]]
print(poke_dataset_csv.head(5))

#Saving updated data into another csv file
#index = False removes the auto generated index column for your rows that may make your data look confusing
#due to the 'Number' column
poke_dataset_csv.to_csv('updated_pokemon_data.csv', index = False)

#Saving updated data into another excel file
#poke_dataset_csv.to_excel('updated_pokemon_data.xlsx', index = False)

#Saving updated data into another text file
#sep, or seperated command adds a replacement for seperator to \t instead of commas
poke_dataset_csv.to_csv('updated_pokemon_dataset.txt', index = False, sep='\t')