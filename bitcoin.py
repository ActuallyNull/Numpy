import requests
import pandas as pd
import matplotlib.pyplot as plt

# Get Bitcoin price data from CoinDesk API
url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2019-02-16&end=2023-02-16'
response = requests.get(url)
data = response.json()

# Convert data to a pandas dataframe
df = pd.DataFrame.from_dict(data['bpi'], orient='index', columns=['Price'])
df.index.name = 'Date'

# Convert dates to a datetime object
df.index = pd.to_datetime(df.index)

# Plot the data using matplotlib
plt.plot(df.index, df['Price'])
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.title('Bitcoin Price Over 2 Years')
plt.show()