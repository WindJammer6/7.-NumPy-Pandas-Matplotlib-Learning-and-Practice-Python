#Exercise 5: Read face cream and facewash product sales data and show it using the bar chart

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sales = pd.read_csv('company_sales_data.csv')

labels_xaxis2 = np.arange(13)
labels_xaxis = labels_xaxis2[1:13]

values_facewash = sales['facewash']
values_facecream = sales['facecream']

plt.bar(labels_xaxis - 0.2, values_facecream, width=0.4, label='Facecream Sales data')
plt.bar(labels_xaxis + 0.2, values_facewash, width=0.4, label='Facewash Sales data')

ticks = []
i = 0
while i <= 3500:
    ticks.append(i)
    i = i + 500
    if i > 3500:
        break

plt.yticks(ticks)
plt.xticks(sales['month_number'])

plt.grid(True, linestyle='--', linewidth=1)
plt.xlabel('Month number')
plt.ylabel('Sold units in number')
plt.title('Facewash and Facecream Sales data')

plt.legend(loc='upper left')

plt.savefig('prac5_bar_graph.png', dpi=100)

plt.show()