#Exercise Question 10: Read all product sales data and show it using the stack plot

import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv('company_sales_data.csv')

labels=[]

for i in sales:
    if i != 'total_profit' and i != 'total_units' and i != 'month_number':
        labels.append(i)

plt.stackplot(sales['month_number'], sales['facecream'], sales['facewash'], sales['toothpaste'], sales['bathingsoap'], sales['shampoo'], sales['moisturizer'], labels=labels, colors=['m','c','r','k','g','y'])

plt.xlabel('Month number')
plt.ylabel('Sales unit in number')
plt.title('All product sales in stack plot')

ticks = []
i = 0
while i <= 30000:
    ticks.append(i)
    i = i + 5000
    if i > 30000:
        break

plt.yticks(ticks)
plt.xticks(sales['month_number'])

plt.legend(loc = 'upper left')

plt.savefig('prac910_bar_graph.png', dpi=100)

plt.show()