
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

# Define the wires
I1 = 1  # Current in wire 1
I2 = 1  # Current in wire 2
start_point1 = np.array([-1, 0, 0])  # Starting point of wire 1
end_point1 = np.array([1, 0, 0])  # Ending point of wire 1
start_point2 = np.array([-1, 0, 1])  # Starting point of wire 2
end_point2 = np.array([1, 0, 1])  # Ending point of wire 2
wire_length1 = np.linalg.norm(end_point1 - start_point1)
wire_length2 = np.linalg.norm(end_point2 - start_point2)

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
            
            # Magnetic field due to wire 1
            dl1 = (end_point1 - start_point1) / wire_length1
            B1 = magnetic_field_wire(I1, start_point1, dl1, r)
            
            # Magnetic field due to wire 2
            dl2 = (end_point2 - start_point2) / wire_length2
            B2 = magnetic_field_wire(I2, start_point2, dl2, r)
            
            # Total magnetic field at the point
            B = B1 + B2
            
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
