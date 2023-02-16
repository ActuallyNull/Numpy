import matplotlib.pyplot as plt

# Create some data to plot
labels = ['Apples', 'Bananas', 'Oranges', 'Grapes']
sizes = [15, 30, 45, 10]

# Plot the data using pie()
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')

# Show the plot
plt.show()