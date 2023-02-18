import pandas as pd
import matplotlib.pyplot as plt

# Read in the Google Trends data into a Pandas dataframe
df = pd.read_csv('CupcakeInterest.csv')

# Create a figure and axis object for the plot
fig, ax = plt.subplots()

# Create a line plot using the plot() function
ax.plot(df['Month'], df['Cupcake: (Worldwide)'], linestyle='--')

# Set the x and y axis labels
ax.set_xlabel('Date')
ax.set_ylabel('Cupcake Search Volume')

# Set the title of the plot
ax.set_title('Search Volume Over Time')

# Add a horizontal line to indicate the trend's average
average = df['Cupcake: (Worldwide)'].mean()
ax.axhline(y=average, color='r', linestyle='-')

# Show the plot
plt.show()
