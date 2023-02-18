#Exercise 10: Merge two data frames using the following condition (see below)

#Create two data frames using the following two Dicts, Merge two data frames, and append the 
#second data frame as a new column to the first data frame.
import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

Car_Price_df = pd.DataFrame.from_dict(Car_Price)

car_Horsepower_df = pd.DataFrame.from_dict(car_Horsepower)

Car_Price_df['horsepower'] = car_Horsepower_df['horsepower']
print(Car_Price_df)

