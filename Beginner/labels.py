# Program Title: Plotting Linear, Quadratic, and Cubic Functions Using Matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Generate 100 evenly spaced values of t between 0 and 2
x = np.linspace(0, 2, 100)

# Plot different functions with labels
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

# Add labels for axes
plt.xlabel('x label')
plt.ylabel('y label')

# Add title for the graph
plt.title("Simple Plot")

# Show ledgend to identify each curve
plt.legend()

# Display the plot
plt.show()
