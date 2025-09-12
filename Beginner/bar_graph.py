# Program: Plots two sets of bars on the same figure with different colors, labels, and a legend.

import matplotlib.pyplot as plt
import matplotlib.style as mplstyle

# Set the style of the plot to 'ggplot' for a grid background and clean look
mplstyle.use("ggplot")

# Data for first bar chart
x = [5, 8, 10]    # X-axis positions for first set of bars
y = [12, 16, 6]   # Heights of bars for first set

# Data for second bar chart
x1 = [6, 9, 11]   # X-axis positions for second set of bars
y1 = [6, 15, 7]   # Heights of bars for second set

# Plot for the bar chart
plt.bar(x, y, color='r', label='Bar One', align='center') # 'r' = red bars, label for legend, centered alignment
plt.bar(x1, y1, color='c', label='Bar Two', align='center') # 'c' = cyan bars, label for legend, centered alignment

# Add title and axis labels
plt.title("Epic info")
plt.xlabel('Y axis')
plt.ylabel('x axis')

# Add legend and grid
plt.legend()                # Display legend for the bars
plt.grid(True, color='k')   # Show grid lines, 'k' = black color

# Display the plot
plt.show()
