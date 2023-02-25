#Exercise 3: Read all product sales data and show it using a multiline plot

import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv('company_sales_data.csv')

plt.figure(figsize=(5,3))

for product in sales:
    if product != 'total_profit' and product != 'total_units' and product != 'month_number':
        plt.plot(sales['month_number'], sales[product], marker='.', label=product)

plt.xlabel('Month number')
plt.ylabel('Sold units in number')
plt.title('Sales data for each product')

plt.yticks([1000,2000,4000,6000,8000,10000,12000,15000,18000])
plt.xticks(sales['month_number'])

plt.legend()

plt.savefig('prac3_bar_graph.png', dpi=100)

plt.show()