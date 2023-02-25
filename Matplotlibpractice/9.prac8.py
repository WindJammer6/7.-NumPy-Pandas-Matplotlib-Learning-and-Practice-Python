#Exercise 8: Calculate total sale data for last year for each product and show it using a Pie chart

import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv('company_sales_data.csv')

sales2 = sales.iloc[:, 1:7].copy()

#Transposing the table (rotating table by 90 degrees such that rows becomes the columns and columns become the rows)
sales3 = sales2.T.copy()

columns = sales3.columns
sales3['total_units'] = sales3[0] + sales3[1] + sales3[2] + sales3[3] + sales3[4] + sales3[5] + sales3[6] + sales3[7] + sales3[8] + sales3[9] + sales3[10] + sales3[11]

product = []

for i in sales3['total_units']:
    product.append(i)

labels = ['Facecream', 'Facewash', 'Toothpaste', 'Bathingsoap', 'Shampoo', 'Moisturizer']

explode = [.1,.1,.1,.1,.1,.1]
plt.pie(product, labels=labels, autopct='%.1f %%', explode=explode, shadow=True)

plt.title('Sales data')

#'bbox_to_anchor=(1, 0.5)' function allows you to shift the position of the legend in the graph. The first
#parameter shifts it at the xaxis, while second parameter shifts it at the yaxis
plt.legend(bbox_to_anchor=(0.1, 1))

plt.savefig('prac8_bar_graph.png', dpi=100)

plt.show()


#Regarding getting the sum for all units for the months for ech product can simply do this also (from answer), 
#without transposing and stuff:
#salesData   = [df ['facecream'].sum(), df ['facewash'].sum(), df ['toothpaste'].sum(), 
#               df ['bathingsoap'].sum(), df ['shampoo'].sum(), df ['moisturizer'].sum()]