import numpy as np
import matplotlib.pyplot as plt
import random

# Create some data to plot
x = np.linspace(random.randint(-52,39), random.randint(-93,52), 100)
y = np.linspace(random.randint(-76,41), random.randint(-84,83), 100)
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
plt.scatter(Y, X, Z, randColor, randMarker, cmap='plasma')
plt.pie(1, 10)

# Show the plot
plt.savefig("scatter.png")
plt.show()