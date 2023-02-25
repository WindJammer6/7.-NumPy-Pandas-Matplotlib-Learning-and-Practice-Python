#Exercise 9: Read Bathing soap facewash of all months and display it using the Subplot

import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv('company_sales_data.csv')

#These functions makes the spacing between the subplots not so close together and cause labels to overlap
fig, axes = plt.subplots(nrows=2, ncols=1)
fig.tight_layout() # Or equivalently,  "plt.tight_layout()"

#Plot 1
#Figure has 2 rows, 1 column, and this plot is the first plot.
plt.subplot(2,1,1)
plt.plot(sales['month_number'], sales['bathingsoap'], marker='.', markersize=10, color='black', linewidth=3)
plt.title('Bathingsoap Sales data')

plt.yticks([7500,10000,12500])
plt.xticks(sales['month_number'])


#Plot 2
#Figure has 2 rows, 1 column, and this plot is the second plot.
plt.subplot(2,1,2)
plt.plot(sales['month_number'], sales['facewash'], marker='.', markersize=10, color='r', linewidth=3)
plt.title('Facewash Sales data')

plt.xlabel('Month number')
plt.ylabel('Sales unit in number')

plt.yticks([1500,2000])
plt.xticks(sales['month_number'])

plt.savefig('prac9_bar_graph.png', dpi=100)

plt.show()
