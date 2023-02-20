import pandas as pd

poke_dataset_csv = pd.read_csv('pokemon_data.csv')

#Gives high level mathematical description of your data (min, max, mean, std, etc)
poke_dataset_csv.describe()
print(poke_dataset_csv.describe())


#Sorting alphabetically
a = poke_dataset_csv.sort_values('Name')  #sorts with ascending alphabetical order
b = poke_dataset_csv.sort_values('Name', ascending=False)  #sorts with descending alphabetical order
print(a)
print(b)


#Sorting alphabetically, with multiple columns
c = poke_dataset_csv.sort_values(['Type 1', 'HP'], ascending=True)  #sets to ascending to True for both columns
d = poke_dataset_csv.sort_values(['Type 1', 'HP'], ascending=[1,0]) #sets to ascending to True for column 'Type 1'
                                                                #while setting ascending to False for column 'HP"
print(c)
print(d)