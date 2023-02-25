#Exercise 1: Read Total profit of all months and show it using a line plot

import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv('company_sales_data.csv')

plt.figure(figsize=(5,3))

plt.plot(sales['month_number'], sales['total_profit'])

plt.xlabel('Month number')
plt.ylabel('Total profit')
plt.title('Company profit per month')

plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.xticks(sales['month_number'])

plt.savefig('prac1_bar_graph.png', dpi=100)

plt.show()

