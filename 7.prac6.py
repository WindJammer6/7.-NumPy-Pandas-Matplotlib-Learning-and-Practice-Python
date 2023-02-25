#Exercise 6: Read sales data of bathing soap of all months and show it using a bar chart. 
#Save this plot to your hard disk.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sales = pd.read_csv('company_sales_data.csv')

labels2 = np.arange(13)
labels = labels2[1:13]

values = sales['bathingsoap']

plt.bar(labels, values)

ticks = []
i = 0
while i <= 14000:
    ticks.append(i)
    i = i + 2000
    if i > 14000:
        break

plt.yticks(ticks)
plt.xticks(sales['month_number'])

plt.grid(True, linestyle='--', linewidth=1)
plt.xlabel('Month number')
plt.ylabel('Sold units in number')
plt.title('Bathingsoap Sales data')

plt.savefig('prac6_bar_graph.png', dpi=300)

plt.show()