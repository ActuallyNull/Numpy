import numpy as np
import matplotlib.pyplot as plt
import random

# Create some data to plot
x = np.linspace(random.randint(-52,39), random.randint(-93,52), 100)
y = np.linspace(random.randint(-76,41), random.randint(-84,83), 100)
X, Y = np.meshgrid(x, y)



# Plot the data using contour()
plt.scatter(Y, X, cmap='plasma')
plt.pie(1, 10)

# Show the plot
plt.savefig("scatter.png")
plt.show()