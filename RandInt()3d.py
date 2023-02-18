import numpy as np
import matplotlib.pyplot as plt
import random

# Create some data to plot
x = np.linspace(random.randint(-52,39), random.randint(-93,52), 100)
y = np.linspace(random.randint(-76,41), random.randint(-84,83), 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create a 3D cartesian plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z)



# Show the plots
plt.show()