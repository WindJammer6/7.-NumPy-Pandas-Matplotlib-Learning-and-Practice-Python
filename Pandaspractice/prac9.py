#Exercise 9: Concatenate two data frames using the following conditions (see below)
#Create two data frames using the following two dictionaries.

#Concatenate means to combine 2 things together. In this context, is to join the 2 dataframes together
import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

#Converting dictionaries to dataframes
GermanCars_df = pd.DataFrame.from_dict(GermanCars)

japaneseCars_df = pd.DataFrame.from_dict(japaneseCars)

new_df = pd.concat([GermanCars_df, japaneseCars_df], keys = ["Germany", "Japan"], axis=0)
new_df2 = pd.concat([GermanCars_df, japaneseCars_df], keys = ["Germany", "Japan"], axis=1)
print(new_df)
print(new_df2)


#The code below dosent work. (attempt to use pd.concat() as concat requires the 2 arguments to already be dataframes
#but GermanCars and japaneseCars are dictionaries and not yet dataframes)
#df = pd.read_csv('Automobile_data.csv')
#new_df = pd.concat([GermanCars, japaneseCars])
#print(new_df)