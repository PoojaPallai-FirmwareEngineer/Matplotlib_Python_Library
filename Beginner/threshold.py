# Program: Plotting Large Random Data with Path Simplification & Path Simplification Threshold

import numpy as np                   # For numerical operations and random data generation
import matplotlib.pyplot as plt      # For plotting
import matplotlib as mpl             # For controlling global rcParams (plot settings)

# Generate 100,000 random values between 0 and 1
y = np.random.rand(100000)

# Scale the second half of the array (values after index 50,000) by factor of 2
y[50000:] *= 2

# Select 400 indices on a log scale between 10^1 (=10) and log10(50000)
# At those indices, subtract 1 (to create some dips in data for visualization)
y[np.logspace(1, np.log10(50000), 400).astype(int)] -= 1

# Enable path simplification (Matplotlib will reduce number of points while drawing lines)
mpl.rcParams['path.simplify'] = True

# Set simplification threshold = 0 (no simplification, full detail)
mpl.rcParams['path.simplify_threshold'] = 0.0
plt.plot(y)
plt.show()

# Change simplification threshold = 1.0 (maximum simplification, fewer points shown)
mpl.rcParams['path.simplify_threshold'] = 1.0
plt.plot(y)
plt.show()
