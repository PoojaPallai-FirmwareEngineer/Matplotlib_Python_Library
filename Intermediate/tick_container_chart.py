# Program Title: Customizing Y-Axis Tick Containers in Matplotlib
# Description: This program demonstrates how to access and modify y-axis tick containers 
#              in Matplotlib. It shows how to move y-axis ticks to the right, hide/show 
#              tick labels, change their color, and format tick labels as currency.

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Set seed for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()

# Plot random data
ax.plot(100 * np.random.rand(2))
ax.plot(100 * np.random.rand(20))

# Create a formatter to display y-axis labels as currency with 2 decimal places
formatter = ticker.FormatStrFormatter('$%1.2f')
ax.yaxis.set_major_formatter(formatter)

# Move y-axis ticks and labels to the right side
ax.yaxis.tick_right()

# Access y-axis major tick containers and modify their properties
for tick in ax.yaxis.get_major_ticks():
    tick.label1On = False       # hide left
    tick.label2On = True        # show right
    tick.label2.set_color("green")  # Set right-side label color to green

plt.show()
