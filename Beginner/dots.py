# ====================================================
# Program: Plotting with Matplotlib and NumPy
# Description: Demonstrates different plotting styles such as line plots, dots, and symbols in graphs using matplotlib.
# ====================================================

import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------
# Example 1: Simple Line Plot
# Plots y = [1, 2, 3, 4] against x = [0, 1, 2, 3]
# --------------------------------------------
plt.plot([1, 2, 3, 4])   # Line plot
plt.ylabel('Some numbers')  # Y-axis label
plt.show()

# --------------------------------------------
# Example 2: Plot with Red Dots
# Plots y-values [1, 4, 9, 10] against x-values [1, 2, 3, 4]
# 'ro' means red color + circle marker
# Axis range is set to [xmin=0, xmax=6, ymin=0, ymax=20]
# --------------------------------------------
plt.plot([1, 2, 3, 4], [1, 4, 9, 10], 'ro')
plt.axis([0, 6, 0, 20])  
plt.show()

# --------------------------------------------
# Example 3: Multiple Plots with Different Styles
# Using NumPy to generate values of t from 0.0 to 5.0 (step=0.2)
# - Red dashed line ('r--') for y = t
# - Blue squares ('bs') for y = t^2
# - Green triangles ('g^') for y = t^3
# --------------------------------------------
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--',      # y = t, red dashed line
         t, t**2, 'bs',    # y = t^2, blue square markers
         t, t**3, 'g^')    # y = t^3, green triangle markers

# Adding title and labels for clarity
plt.title("Matplotlib Plot Styles Example")
plt.xlabel("X-axis (t)")
plt.ylabel("Y-axis (functions of t)")

# Display the plot
plt.show()
