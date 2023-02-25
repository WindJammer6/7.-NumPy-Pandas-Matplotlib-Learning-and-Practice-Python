#Exercise 7: Read the total profit of each month and show it using the histogram to see the 
#most common profit ranges

import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv('company_sales_data.csv')

bins = [150000, 175000, 200000, 225000, 250000, 300000, 350000]

plt.hist(sales['total_profit'], bins=bins, label='Profit data')

plt.xticks(bins)

plt.xlabel('Profit range (in dollar)')
plt.ylabel('Number of months')
plt.title('Profit data')

plt.legend(loc='upper left')

plt.savefig('prac7_bar_graph.png', dpi=100)

plt.show()