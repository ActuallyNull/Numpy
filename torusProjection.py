import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define torus parameters
r1 = 5
r2 = 1  

# generate torus coords
theta, phi = np.meshgrid(np.linspace(0, 2*np.pi, 30), np.linspace(0, 2*np.pi, 30))
# calculates x,y,z coords
# r1 + r2*np.cos(phi) = calculates the distance from the center of the torus to the center of the rotating circle
# cos(theta) and sin(theta) components rotate the circle around the center of the torus to generate the points on the surface.
x = (r1 + r2*np.cos(phi)) * np.cos(theta)
y = (r1 + r2*np.cos(phi)) * np.sin(theta)
# the z-axis of the coordinate system points out of the plane, sin(phi) component controls the distance from the center of the torus
z = r2*np.sin(phi)

# plot torus
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='plasma')
plt.show()