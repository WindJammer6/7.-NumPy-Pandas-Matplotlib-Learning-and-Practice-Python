import pandas as pd 

poke_dataset_csv = pd.read_csv('pokemon_data.csv')

#Read headers
print(poke_dataset_csv.columns)


#Read each column
print(poke_dataset_csv['Name'])

#Reading multiple columns of your choice
print(poke_dataset_csv[['Name', 'Type 1', 'HP']])

#Read each column, specifying which rows to take
print(poke_dataset_csv['Name'][0:5])  #take first 5 rows in column 'Name'

#Read multiple column, specifying which rows to take
print(poke_dataset_csv[['Name', 'Type 1', 'HP']][2:5])  #take rows 2, 3 and 4 (since index 0 represents 1st row and index 4 
                                      #represents 5th row in column 'Name')


#Read each row (iloc stands for interger location)
print(poke_dataset_csv.iloc[1])

#Read multiple rows of your choice
print(poke_dataset_csv.iloc[0:4])


#Read a specific location(row, column) (for row, it takes the index for input, not the numbering in the file)
print(poke_dataset_csv.iloc[2,1])


#A trick to use when working with data
for index, row in poke_dataset_csv.iterrows():
    print(index, row)
    print(index, row['Name'])  #To only get index and the corresponding name in 'Name' column


#iloc vs loc
#loc selects rows and columns with specific labels. 
#iloc selects rows and columns at specific integer positions
a = poke_dataset_csv.loc[poke_dataset_csv['Type 1'] == 'Fire']
print(a)
#Taking multiple conditions 
b = poke_dataset_csv.loc[(poke_dataset_csv['Type 1'] == 'Fire') | (poke_dataset_csv['Type 1'] == 'Grass')]
print(b)