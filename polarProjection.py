import numpy as np
import matplotlib.pyplot as plt

x = 5
y = 10

fig, ax = plt.subplots()

ax = fig.add_subplot(111, projection='polar')
# Generate the spiral curve
theta = np.linspace(0, 10*np.pi, 1000)
r = theta

# Plot the spiral curve
ax.plot(theta, r)

# Show the plot
plt.show()