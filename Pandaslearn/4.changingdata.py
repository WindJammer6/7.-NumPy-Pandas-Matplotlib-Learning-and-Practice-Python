import pandas as pd

poke_dataset_csv = pd.read_csv('pokemon_data.csv')

#Adding a 'Total' column of all the stats added together 
poke_dataset_csv['Total'] = poke_dataset_csv['HP'] + poke_dataset_csv['Attack'] + poke_dataset_csv['Defense'] + poke_dataset_csv['Sp. Atk'] + poke_dataset_csv['Sp. Def'] + poke_dataset_csv['Speed']

print(poke_dataset_csv.head(5))

#The 'Total' column is now in memory and is part of poke_dataset_csv, even if you remove the top code and print poke_dataset_csv
#Hence to remove it, you need to create another variable to remove/drop that column

#Removing a column
poke_dataset_csv = poke_dataset_csv.drop(columns=['Total'])
print(poke_dataset_csv.head(5))


#Summing multiple columns and making a new column
#In iloc[0:10, 4:10], 
#the first 0:10 indicates you are selecting the indexes of the rows you want to have data in this new column, placing only : indicates you want all rows
#the second 4:10 indicates you are selecting the indexes of the columns

#.sum(axis=1) means you want to add the rows together as values in the new column 'Total'
#.sum(axis=0) means you want to add the columns together as values in the new column Total'
poke_dataset_csv['Total'] = poke_dataset_csv.iloc[:, 4:10].sum(axis=1)  
print(poke_dataset_csv.head(5))


#Rearranging the columns
#columns[-1] gets the 'Total' column, since it is taking only 1 column, you need add additional squre brackets []
columns = list(poke_dataset_csv.columns)
poke_dataset_csv = poke_dataset_csv[columns[0:4] + [columns[-1]] + columns[4:12]]
print(poke_dataset_csv.head(5))