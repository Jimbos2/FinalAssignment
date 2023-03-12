import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('liquor_iowa.csv')

# most popular product in zip code

# this code is for the number 1 product in every zip code
madd = data.loc[data.groupby('zip_code')['bottles_sold'].transform('max').eq(data['bottles_sold'])]

# this code is for multiple products in each zip code
'''
dafa = data.groupby(['zip_code', 'item_number']).agg({"bottles_sold": ['max']})
dafa.columns = ['bottles_sold']
dafa = dafa.reset_index()

'''
colors = madd.groupby('item_number')
# colors = dafa.groupby('item_number')

for name, group in colors:
   plt.plot(group.zip_code, group.bottles_sold, marker= 'o', ls='',markersize=12, label=name)


plt.show()



# percentage of sales per store

sal = data.groupby('store_number').sum().sort_values('store_number')

# print(sal.sale_dollars)
total = np.sum(sal['sale_dollars'])
sal.sale_dollars = np.multiply((np.divide(sal['sale_dollars'],total)),100)
sal.sale_dollars = np.around(sal.sale_dollars, decimals=4)
# print(sal.sale_dollars.sort_values())

plt.bar(sal.index, sal.sale_dollars, width=100)
plt.show()