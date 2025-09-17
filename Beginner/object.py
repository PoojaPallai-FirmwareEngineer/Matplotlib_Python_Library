# Program: Plotting a Sine Wave and Histogram using Matplotlib with ggplot Style
# Description:
# This program demonstrates creating multiple subplots in a single figure using Matplotlib.
# The first subplot shows a sine wave, and the second subplot shows a histogram of normally distributed random data.
# The 'ggplot' style is applied for better aesthetics.

import numpy as np
import matplotlib.pyplot as plt

# Use ggplot style
plt.style.use('ggplot')

fig = plt.figure()
fig.subplots_adjust(top=0.8)

# First subplot: sine wave
ax1 = fig.add_subplot(211)
ax1.set_ylabel('volts')
ax1.set_title('A sine wave')

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
line, = ax1.plot(t, s, color='b')
ax1.set_xlabel('time (s)')

# Second subplot: histogram
np.random.seed(19680801)    # Set seed for reproducibility
ax2 = fig.add_subplot(212)

# Generate histogram with 50 bins, yellow bars with yellow edges
n, bins, patches = ax2.hist(np.random.randn(1000), 50, facecolor='yellow', edgecolor='yellow')
ax2.set_xlabel('value')
ax2.set_ylabel('frequency')
ax2.set_title('A histogram')

plt.show()
