import pandas as pd

updated_poke_dataset_csv = pd.read_csv('updated_pokemon_data.csv')

#Giving new empty dataframe with the same columns (and column names) as the original dataframe
new_df = pd.DataFrame(columns=updated_poke_dataset_csv.columns)

#concat functions sort of appends two dataframes together, which it did for 'new_df' and 'results' dataframe
for df in pd.read_csv('updated_pokemon_data.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
#This line appends the 2 dataframes together, and stores it back into the ''new_df' dataframe
    new_df = pd.concat([new_df, results])

print(new_df)