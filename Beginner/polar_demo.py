# Program: Line Plot on a Polar Axis using Matplotlib
# Description:
# This program demonstrates how to create a **polar plot** in Matplotlib.
# It plots a line in polar coordinates, adjusts the radius, customizes radial ticks, and adds a title.

import matplotlib.pyplot as plt
import numpy as np

r = np.arange(0,2,0.01)                         # Generate radius values from 0 to 2 with step 0.01
theta = 2 *np.pi*r                              # Calculate theta values (angle in radians) for each radius
ax=plt.subplot(111,projection='polar')
ax.plot(theta, r)
ax.set_rmax(2)                                  # Set maximum radius for the plot
ax.set_rticks([0.5, 1, 1.5, 2])                 # Set radial ticks at 0.5, 1, 1.5, and 2
ax.set_rlabel_position(-22.5)                   # Set the position of radial labels (angle in degrees)
ax.grid(True)                                   # Enable grid for better readability
ax.set_title("A line plot on a polar axis")
plt.show()
