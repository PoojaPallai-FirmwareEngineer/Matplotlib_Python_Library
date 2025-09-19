# Program: 3D Surface Plot of a Sine Function Using Matplotlib

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# ---- Create figure and 3D axis ----
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ---- Generate grid data ----
X = np.arange(-5, 5, 0.25)                    # X values from -5 to 5 with step 0.25
Y = np.arange(-5, 5, 0.25)                    # Y values from -5 to 5 with step 0.25
X, Y = np.meshgrid(X, Y)                      # Create meshgrid
R = np.sqrt(X**2 + Y**2)                      # Distance from origin
Z = np.sin(R)                                 # Function to plot: Z = sin(R)

# ---- Plot the 3D surface ----
surg = ax.plot_surface(
    X, Y, Z,
    cmap=cm.coolwarm,                         # Apply coolwarm colormap
    linewidth=0,                              # No wireframe lines
    antialiased=False                         # Disable anti-aliasing
)

# ---- Customize Z axis ----
ax.set_zlim(-1.01, 1.01)                      # Limit Z axis range
ax.zaxis.set_major_locator(LinearLocator(10)) # 10 tick marks on Z axis
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  # Format ticks to 2 decimals

# ---- Add color bar ----
fig.colorbar(surg, shrink=0.5, aspect = 5)

# ---- Display the plot ----
plt.show()
