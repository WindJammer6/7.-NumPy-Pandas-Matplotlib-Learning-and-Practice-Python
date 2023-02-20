import pandas as pd
import re

poke_dataset_csv = pd.read_csv('pokemon_data.csv')

#'RegEx', or regular expressions, filtering helps to filter based on textual pattern
#in order to use these patterns, you need to import re

#.str.contains() is able to find a certain strings from rows in the
#columns and print rows with that string out
a = poke_dataset_csv.loc[poke_dataset_csv['Name'].str.contains('Mega')]
print(a)

#To take rows that does not have that certain string you add the wiggly line 
b = poke_dataset_csv.loc[~poke_dataset_csv['Name'].str.contains('Mega')]
print(b)

#new_data2 = poke_dataset_csv.loc[(poke_dataset_csv['Type 1'] == 'Grass') & (poke_dataset_csv['Type 2'] == 'Poison') & (poke_dataset_csv['HP'] > 70)]
#Recall this,code, and that we can also use these RegEx functions to filter out data similarly

#Flag variable is used as a signal in programming to let the program know that a certain condition has met. 
#It usually acts as a boolean variable indicating a condition to be either true or false

#re.I, the I stands for 'IGNORECASE', ignore upper and lower case of input (fire or grass in this case) 
#while searching the input through the columns

#The regex Function applies a regular expression to a string and returns the matching substrings
c = poke_dataset_csv.loc[poke_dataset_csv['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
print(c)

#^ means starting of string (without this, just pi[a-z]* youll just get pokemon with 'pi' in their name)
#^pi means you are looking for pokemon with name starting with 'pi' at the beginning of their name
#[a-z] means the character next can be any character of letter a to z
#[a-z]* means zero or more characters behind the first 2 letters 'pi' can be any character from letter a to z 
d = poke_dataset_csv.loc[poke_dataset_csv['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print(d)




