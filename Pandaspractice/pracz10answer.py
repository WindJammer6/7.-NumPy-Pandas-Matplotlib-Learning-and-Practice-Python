#Exercise 10: Merge two data frames using the following condition (see below)

#Create two data frames using the following two Dicts, Merge two data frames, and append the 
#second data frame as a new column to the first data frame.import pandas as pd
import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

carPriceDf = pd.DataFrame.from_dict(Car_Price)

carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
print(carsDf)

#Combining data in pandas with merge() and concat():
#merge() is for putting together 2 dataframes side by side. It will print out a resulting dataframe. 
#By default, if there is any commonalities in the common columns and stitches them together in the result. 
#If no commonalities, then it will not print that row in the resulting dataframe

#However, for merge() most of the time we specify 'on=' which common column in both dataframes that 
#we wish to combine the dataframes e.g. "Company", which is present in both dataframes in this practice.
#e.g. 'on=horsepower' will not work as 'carPriceDf' does not have this column, only 'carsHorsepowerDf' does, hence 
#they will not be able to merge on this column


#concat() is for putting together 2 dataframes top and bottom. If 1 of the dataframes has columns that the 
#other dosent have, the values for that dataframe in the resulting dataframe will display a NaN (null) value.
