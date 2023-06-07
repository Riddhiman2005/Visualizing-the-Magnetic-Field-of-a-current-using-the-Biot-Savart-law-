

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
mu0 = 4 * np.pi * 10**-7  # Vacuum permeability

# Function to calculate magnetic field at a point due to a current-carrying wire
def magnetic_field_wire(I, r0, dl, r):
    r_vector = r - r0
    dl_cross_r = np.cross(dl, r_vector)
    magnitude = (mu0 * I) / (4 * np.pi * np.linalg.norm(r_vector)**3)
    return magnitude * dl_cross_r

# Define the current-carrying wire
I = 1  # Current
start_point = np.array([0, 0, -1])  # Starting point of the wire
end_point = np.array([0, 0, 1])  # Ending point of the wire
wire_length = np.linalg.norm(end_point - start_point)

# Define the grid of points to calculate the magnetic field
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
z = np.linspace(-2, 2, 20)
X, Y, Z = np.meshgrid(x, y, z)

# Calculate the magnetic field at each point in the grid
Bx = np.zeros_like(X)
By = np.zeros_like(Y)
Bz = np.zeros_like(Z)
for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(z)):
            r = np.array([X[i, j, k], Y[i, j, k], Z[i, j, k]])
            dl = (end_point - start_point) / wire_length
            B = magnetic_field_wire(I, start_point, dl, r)
            Bx[i, j, k] = B[0]
            By[i, j, k] = B[1]
            Bz[i, j, k] = B[2]

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the magnetic field vectors
ax.quiver(X, Y, Z, Bx, By, Bz, length=0.1, normalize=True)

# Set the axis labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Set equal aspect ratio for better visualization
ax.set_box_aspect([np.ptp(X), np.ptp(Y), np.ptp(Z)])

# Show the plot
plt.show()
