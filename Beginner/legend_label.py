# Program: Plotting Multiple Lines with Customized Legend in Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Create an array of values from 0 to 3 with step size 0.2
a = b = np.arange(0, 3, .2)

# Exponential values of 'a'
c = np.exp(a)

# Reverse of c
d = c[::-1]

# Create a figure and axis object using subplots
fig, ax = plt.subplots()

# Plot first line (dashed black line) with label
ax.plot(a,c,'k--', label='Model length')

# Plot second line (doted black line) with label
ax.plot(a,d,'k:', label='Data length')

# Plot third line (solid black line) with label
ax.plot(a,c + d,'k', label='total message length')

# Add legend at upper center with shadow and larger font
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

# Customize legend background color to cyan
legend.get_frame().set_facecolor('c')

# Show the plot
plt.show()
