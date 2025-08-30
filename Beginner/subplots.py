# ====================================================
# Program: Subplots with Matplotlib
# Description:
#   - Demonstrates how to use multiple subplots
#   - Plots an exponentially decaying cosine function and a standard cosine function using different styles.
# ====================================================

import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------
# Function: f(t)
# Returns an exponentially decaying cosine:
#   f(t) = e^(-t) * cos(2πt)
# --------------------------------------------
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

# --------------------------------------------
# Generate time values:
# t1: step size = 0.1
# t2: finer step size = 0.02 (for smoother curve)
# --------------------------------------------
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

# Create a new figure (Figure 1)
plt.figure(1)

# --------------------------------------------
# Subplot 1 (Top: position 211 → 2 rows, 1 column, 1st plot)
# - Blue circle markers ('bo') for coarse data points
# - Black solid line ('k') for smooth curve
# --------------------------------------------
plt.subplot(211)
plt.plot(t1, f(t1), 'bo',    # Blue circles (coarse points)
         t2, f(t2), 'k')     # Black line (smooth curve)
plt.title("Exponential Decay Cosine Function")

# --------------------------------------------
# Subplot 2 (Bottom: position 212 → 2 rows, 1 column, 2nd plot)
# - Red dashed line ('r--') for cosine function
# --------------------------------------------
plt.subplot(212)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')  # Red dashed cosine
plt.title("Cosine Function")

# Add overall figure title
plt.suptitle("Matplotlib Subplot")

# Show plots
plt.show()
