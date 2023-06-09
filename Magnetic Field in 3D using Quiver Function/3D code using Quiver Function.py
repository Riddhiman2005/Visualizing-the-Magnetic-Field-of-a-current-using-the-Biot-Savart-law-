
# This code uses and defines the strenght of current and location with the mesh grid points 
# where magnetic field will be calculated
# We used quiver function to plot the magnetic field in 3D
# Computes the magnetic field components generated by the wire and generates a 
# 3D version of the field utilizing the "quiver" function. 


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Defining the magnet strength and location
I = 1.0  # current strength
x_c = 0.0  # x-coordinate of current
y_c = 0.0  # y-coordinate of current


# Defining the mesh grid of points
x, y, z = np.meshgrid(np.linspace(-4, 4, 20),
                      np.linspace(-4, 4, 20),
                      [0])

# Defining the Magnetic field components due to the current
r = np.sqrt((x-x_c)**2 + (y-y_c)**2 + (z)**2)
B_x = I * (y-y_c) / r**3
B_y = -I * (x-x_c) / r**3
B_z = np.zeros_like(r)

# Creating the figure and axes
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Creating the quiver plot of the magnetic field
ax.quiver(x, y, z, B_x, B_y, B_z, length=0.2, normalize=True)

# Plot the current carrying wire

z_wire = np.linspace(-4, 4, 50)
x_wire = np.zeros_like(z_wire)
y_wire = np.zeros_like(z_wire)
ax.plot(x_wire, y_wire, z_wire, lw=3, color='green')


# Plot limits and axis labels
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-4, 4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Show  plot
plt.show()