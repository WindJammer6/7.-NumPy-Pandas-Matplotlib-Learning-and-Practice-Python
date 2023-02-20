import pandas as pd

#Chunksize refers to number of rows in the file to select at once
#Printed a "CHUNK DATAFRAME" to indicate the different chunks of 5 being printed
for updated_poke_dataset_csv in pd.read_csv('updated_pokemon_data.csv', chunksize=5):
    print("CHUNK DATAFRAME")
    print(updated_poke_dataset_csv)
