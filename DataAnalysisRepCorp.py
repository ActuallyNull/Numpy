import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CSV Files/statsfinal.csv")

subsetSales = df.iloc[1:51, 1:5] #select rows 1 to 50 and columms 1 to 4
subsetProfit = df.iloc[1:51, 5:10] #select rows 1 to 50 and columms 5 to 9
dfDate = df['Date']
models = ['P1', 'P2', 'P3', 'P4']
colors = ['red', 'green', 'blue', 'orange']
MedianP1Sales = subsetSales['Q-P1'].mean()
MedianP2Sales = subsetSales['Q-P2'].mean()
MedianP3Sales = subsetSales['Q-P3'].mean()
MedianP4Sales = subsetSales['Q-P4'].mean()
MedianP14SalesArray = [MedianP1Sales, MedianP2Sales, MedianP3Sales, MedianP4Sales]

MedianP1Profit = subsetProfit['S-P1'].mean()
MedianP2Profit = subsetProfit['S-P2'].mean()
MedianP3Profit = subsetProfit['S-P3'].mean()
MedianP4Profit = subsetProfit['S-P4'].mean()
MedianP14ProfitArray = [MedianP1Profit, MedianP2Profit, MedianP3Profit, MedianP4Profit]
print(MedianP14ProfitArray)
fig, ax = plt.subplots()

fig2, ax2 = plt.subplots()
# plot the subsets of the data and set the labels
for i in range(len(MedianP14SalesArray)):
    ax2.bar(models[i], MedianP14SalesArray[i], color=colors[i], label='Revenue from P{}'.format(i+1))
ax.set_ylabel('Amount of models sold')



for i in range(len(MedianP14ProfitArray)):
    ax.bar(models[i], MedianP14ProfitArray[i], color=colors[i], label='Quantity of P{} Sold'.format(i+1))
ax2.set_ylabel('Revenue from models sold ($)')

# set the title and legend
ax.set_title('Quantity of P1-4 Sold')
ax.legend()
ax2.set_title('Amount of money from models P1-4')
ax2.legend()
plt.show()
