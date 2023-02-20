import pandas as pd #so you dont have to type 'panda' and can type 'pd'
                    #instead to refer to a function from panda

#Loading the data into your code. Pandas accept csv, text(text in a table) and Excel files
#-to load excel poke_dataset_excel = pd.read_excel("")
#-to load csv poke_dataset_csv = pd.read_csv("")
#-to load text poke_dataset_txt = pd.read_csv("", delimiter='\t')

#(delimiter basically removes what is seperating your columns. If you
# print the text file without delimiter it actually gives you alot of \t,
# in between the columns so add delimiter \t to remove them)

poke_dataset_csv = pd.read_csv('pokemon_data.csv')
print(poke_dataset_csv)
print("")

#Print top 3 rows of dataset
print(poke_dataset_csv.head(3))

#Print bottom 3 rows of dataset
print(poke_dataset_csv.tail(3))