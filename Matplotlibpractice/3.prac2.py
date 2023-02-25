#Exercise 2: Get total profit of all months and show line plot with the following Style properties

import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv('company_sales_data.csv')

plt.figure(figsize=(5,3))

plt.plot(sales['month_number'], sales['total_profit'],  'r.--', label='Profit data of last year', linewidth=3, markersize=10, markerfacecolor='black')

plt.xlabel('Month number')
plt.ylabel('Sold units in number')
plt.title('Company profit per month')

plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.xticks(sales['month_number'])

plt.legend(loc='lower right')

plt.savefig('prac2_bar_graph.png', dpi=100)

plt.show()