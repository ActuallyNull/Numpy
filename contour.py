import numpy as np
import matplotlib.pyplot as plt
import random

# Create some data to plot
#x = np.linspace(random.randint(1,39), random.randint(1,52), 100)
x = np.arange(random.randint(1,39), random.randint(1,52), 0.1)
#y = np.linspace(random.randint(1,41), random.randint(1,83), 100)
y = np.arange(random.randint(1,41), random.randint(1,83), 0.1)
X, Y = np.meshgrid(x, y)

Z = np.tan(np.sqrt(X**2 + Y**2))
W = np.sin(Z)
V = np.cos(W)
E = np.tan(V)
colorList = ['b','g','r','c','m','y','k','w']
markerList = ['.','o','s','P','X','*','p','D','<','>','^',
              'v','1','2','3','4','+','x','|','_',4,5,6,7,
              '$◐$','$◑$','$◓$','$◒$','$←$','$↑$','$→$','$↓$',]
randColor = random.choice(colorList)
randMarker = random.choice(markerList)

# Plot the data using contour()
plt.scatter(X, Y, Z)

# Show the plot
plt.savefig("scatter.png")
plt.show()