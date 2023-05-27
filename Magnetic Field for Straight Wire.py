
import numpy as np
import matplotlib.pyplot as plt

# Define the current strength and location
I = 1.0  # strength of I
x_c = 0.0  # x-coordinate of I (Ix)
y_c = 0.0  # y-coordinate of I (Iy)

# Define the mesh grid of points
x, y = np.meshgrid(np.linspace(-2, 2, 200), np.linspace(-2, 2, 200))

# Define the magnetic field components due to the magnet
r = np.sqrt((x-x_c)**2 + (y-y_c)**2)
B_x = I * (y-y_c) / r**3
B_y = -I * (x-x_c) / r**3

# Plot the magnetic field lines
fig, ax = plt.subplots(figsize=(8, 8))
ax.streamplot(x, y, B_x, B_y, color='red', linewidth=1, density=1, arrowstyle='->')

# Add the wire to the plot
circle = plt.Circle((x_c, y_c), 0.1, color='green')
ax.add_artist(circle)

# Set the plot limits and axis labels
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xlabel('x')
ax.set_ylabel('y')

# Show the plot
plt.show()
