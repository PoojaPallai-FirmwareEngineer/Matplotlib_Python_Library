# Program Title: Plotting a Quadratic Function (y = x²) Using Matplotlib

import numpy as np
import matplotlib.pylab as plt

# Generate 100 evenly spaced values of t between 0 and 1
t = np.linspace(0, 1, 100)

# Plot the quadratic function against t
plt.plot(t,t**2)

# Display the plot
plt.show()
