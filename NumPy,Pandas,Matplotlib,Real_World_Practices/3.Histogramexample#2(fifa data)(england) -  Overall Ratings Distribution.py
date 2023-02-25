import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

bins = []
i = 40

while i <= 100:
    bins.append(i)
    i = i + 10
    if i > 100:
        break

a = fifa.loc[fifa['Nationality'].str.contains('England')]

plt.hist(a['Overall'], bins=bins, color='#abcdef')   #light blue colour

plt.xticks(bins)

plt.xlabel('Overall rating')
plt.ylabel('Number of Players')
plt.title('Distribution of England Players Ratings in FIFA 2018', fontdict={'fontsize':15, 'fontweight':'bold'})

plt.savefig('fifa_data_histogram.png', dpi=200)

plt.show()