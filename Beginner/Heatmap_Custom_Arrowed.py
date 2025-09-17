# Program: Heatmap Visualization and Custom Arrowed Axes using Matplotlib

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist import SubplotZero # Allows zero-centered axes with arrowheads

# -----------------------------
# Part 1: Heatmap Visualization
# -----------------------------

N = 47          # Size of the grid

# Create a 2D meshgrid of size N×N
x, y = np.mgrid[:N, :N] 

# Define a mathematical function for z values using cos and sin    
z = (np.cos(x * 0.2) + np.sin(y * 0.3))

# Mask values < 0 (negative) and > 0 (positive) separately for different heatmaps
zpos = np.ma.masked_less(z, 0)           # Keep only positive values
zneg = np.ma.masked_greater(z, 0)        # Keep only negative values

# Create two side-by-side subplots (1 row × 2 columns)
fig, (ax1, ax2) = plt.subplots(figsize=(8, 3), ncols=2)

# Plot positive values in Blue color map
pos = ax1.imshow(zpos, cmap='Blues', interpolation='none')
fig.colorbar(pos, ax=ax1)       # Add colorbar for reference

# Plot negative values in Red color map
neg = ax2.imshow(zneg, cmap='Reds_r', interpolation='none')
fig.colorbar(neg, ax=ax2)       # Add colorbar for reference

# Display the heatmap figure
plt.show()

# -----------------------------
# Part 2: Arrowed Axes Plot
# -----------------------------


if 1:
    fig = plt.figure(1)
    ax = SubplotZero(fig, 111)      # Create a subplot with axis lines that can be customized
    fig.add_subplot(ax)

# Enable arrow-style axes for X=0 and Y=0
for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")        # Add arrowhead to axes
    ax.axis[direction].set_visible(True)                # Make these axes visible

# Hide default borders (top, bottom, left, right) for clarity
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)

# Create X values between -0.5 and 1 with 100 points
x=np.linspace(-0.5, 1, 100)

# Plot sine wave on the custom arrowed axes
ax.plot(x, np.sin(x * np.pi))

# Display the final plot
plt.show()
   