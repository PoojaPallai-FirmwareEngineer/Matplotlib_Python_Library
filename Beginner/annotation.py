# Program: This program plots a cosine wave and adds an annotation with an arrow pointing to a specific point on the curve.

import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
import numpy as np

# Set the plotting style to 'ggplot' for a clean, grid-based background
mplstyle.use("ggplot")

# Create a subplot (1 row, 1 column, 1st subplot)
ax = plt.subplot(111)

# Generate an array of time values from 0 to 5 with step 0.01
t = np.arange(0.0, 5.0, 0.01)

# Compute the cosine values for the time array
s = np.cos(2*np.pi*t)

# Plot the cosine wave with a line width of 2
line = plt.plot(t,s, lw=2)

# Add an annotation with an arrow pointing to the point (2, cos(2*π*2))
# xy = point to annotate
# xytext = location of the text
# arrowprops = properties of the arrow
plt.annotate('local arrow', xy=(2, np.cos(2 * np.pi * 2)), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05))

# Set the y-axis limits for better visualization
plt.ylim(-2.2, 2.2)

# Display the plot
plt.show()
