import matplotlib.pyplot as plt
import pandas as pd

gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(8,5), dpi=100)

plt.title('Gas Prices Over Time (in USD)', fontdict={'fontname':'Comic Sans MS', 'fontsize':20, 'fontweight':'bold'})

plt.xlabel('Time (in years)')
plt.ylabel('Gas Prices (in Gallons)')

#plt.xticks([1990,1995,2000,2005,2008])  try not do this as this is hardcoding
#Note: 'tolist()' converts a series (a 1D array) to a list. In this context in converted 'gas_year_column[::3]' into a list
#so that it can 2011 into the list

#This is better:
gas_year_column = gas['Year']
plt.xticks(gas_year_column[::3].tolist() + [2011])   #Using the steps thing back from what we learnt from NumPy
plt.yticks([1,2,3,4,5,6])

#This is abit of hardcoding. It is possible to print out all countries using a for loop at once
#plt.plot(gas['Year'], gas['USA'], label = 'USA', color = 'r', marker='.') 
#plt.plot(gas['Year'], gas['Canada'], label = 'Canada', color = 'y', marker='.') 
#plt.plot(gas['Year'], gas['South Korea'], label = 'South Korea', color = 'g', marker='.') 
#plt.plot(gas['Year'], gas['Australia'], label = 'Australia', color = 'b', marker='.') 
#Note: plt.plot(gas.Year, gas.USA) works as well for some reason

for country in gas:
    if country != 'Year':
        plt.plot(gas['Year'], gas[country], marker='.', label=country)   #Matplotlib auto selects the color for you
                                                                         #for each graph

plt.legend()

plt.savefig('gas_prices_linegraph.png', dpi=300)

plt.show()