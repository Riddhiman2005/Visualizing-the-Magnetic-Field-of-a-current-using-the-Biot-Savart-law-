
import numpy as np
import matplotlib.pyplot as plt

def plot_parallel_wires(I_1, x_c1, y_c1, I_2, x_c2, y_c2):
  
  # a) For Two parallel Wires carrying current in the same direction, then
  
  plot_parallel_wires(1.0, -1.0, 0.0, 1.0, 1.0, 0.0)
  
  
  # b) For Two Parallel Wires Carrying Current in Opposite Directions, then
  
  plot_parallel_wires(1.0, -1.0, 0.0, -1.0, 1.0, 0.0)
  
  
  
    # Define the mesh grid of points
    
    x, y = np.meshgrid(np.linspace(-2, 2, 200), np.linspace(-2, 2, 200))

    # Define the magnetic field components due to the currents
    
    r1 = np.sqrt((x-x_c1)**2 + (y-y_c1)**2)
    B_x1 = I_1 * (y-y_c1) / r1**3
    B_y1 = -I_1 * (x-x_c1) / r1**3

    r2 = np.sqrt((x-x_c2)**2 + (y-y_c2)**2)
    B_x2 = I_2 * (y-y_c2) / r2**3
    B_y2 = -I_2 * (x-x_c2) / r2**3

    B_x = B_x1 + B_x2
    B_y = B_y1 + B_y2

    # Plot the magnetic field lines
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.streamplot(x, y, B_x, B_y, color='red', linewidth=1, density=1, arrowstyle='->')

    # Add the wires
    circle = plt.Circle((x_c1, y_c1), 0.1, color='green')
    ax.add_artist(circle)
    circle = plt.Circle((x_c2, y_c2), 0.1, color='green')
    ax.add_artist(circle)

    # Set the plot limits and axis labels
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Show the plot
    
    plt.show()

    
    # Plot Generated in case of of Two parallel Wires carrying current in the same direction will be different from two parallel Wires carrying current in the opposite direction.
