#Exercise 4: Read toothpaste sales data of each month and show it using a scatter plot

import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv('company_sales_data.csv')

plt.scatter(sales['month_number'], sales['toothpaste'], label='Toothpaste Sales data')

plt.xlabel('Month number')
plt.ylabel('Sold units in number')
plt.title('Toothpaste Sales data')

plt.grid(True, linestyle='--', linewidth=1)
plt.xticks(sales['month_number'])

plt.legend()

plt.savefig('prac4_bar_graph.png', dpi=100)

plt.show()

