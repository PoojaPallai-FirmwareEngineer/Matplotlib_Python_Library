# Program: Demonstration of Line Styles, Scatter Plots, and Grouped Bar Charts using Matplotlib

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand


# ================================
# Line plots with dash patterns
# ================================

# Generate 500 evenly spaced points between 0 and 10
x = np.linspace(0, 10, 500)

# Define a dash style as alternating dash-gap pairs:
# [dash_length, gap_length, dash_length, gap_length, ...]
# Example: [10, 5, 100, 5] means:
#   → Draw a dash of length 10
#   → Leave a gap of length 5
#   → Draw a dash of length 100
#   → Leave a gap of length 5
# Then repeat the sequence across the line.
dashes = [10, 5, 100, 5]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot sine curve with solid line first
line1, = ax.plot(x, np.sin(x), '-', linewidth=2, label='Dashes set retroactively')

# Plot negative sine curve with dashes set directly while plotting
line2, = ax.plot(x, -1 * np.sin(x), dashes=[30, 5, 10, 5], label='Dashes set proactively')

# Add legend in the bottom right corner
ax.legend(loc='lower right')

# Show th plot
plt.show()

# ================================
# Scatter plot with random points
# ================================

fig, ax = plt.subplots()

# Loop through 3 colors and generate random scatter points for each
for color in ['red', 'green', 'blue']:
    n = 750                                                                        # Number of points     
    x, y = rand(2, n)                                                              # Generate random x, y values
    scale = 200.0 * rand(n)                                                        # Randomize marker sizes
    ax.scatter(x, y, c=color, s=scale, label=color, alpha=0.3, edgecolors='none')  # Scatter plot with transparency

# Add legend and grid
ax.legend()
ax.grid(True)

# Show the plot
plt.show()
    
# ================================
# Grouped bar chart with error bars
# ================================

n = 5                                  # Number of groups

men_means = (20, 35, 30, 35, 27)       # Men's average scores
mem_std = (2, 3, 4, 1, 2)              # Men's score deviations
ind = np.arange(n)                     # X locations for groups
width = 0.35                           # Width of each bar

fig, ax = plt.subplots()

# Plot bars for men
rects1 = ax.bar(ind, men_means, width, color='r', yerr=mem_std)

# Plot bars for women (next to men's bars)
women_means = (25, 32, 34, 20, 25)
women_std = (3, 5, 2, 3, 3)
rects2 = ax.bar(ind + width , women_means, width, color='y', yerr=women_std)

# Set labels, title, and ticks
ax.set_ylabel('scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)                      # Centre the group labels
ax.set_xticklabels(['G1', 'G2','G3', 'G4', 'G5'])
ax.legend((rects1[0], rects2[0]), ('Mens', 'Womens'))

# Function to attach text labels above bars
def autolabels(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, 1.05 * height, '%d' % int (height), ha='center', va='bottom')

# Add labels to both sets of bars
autolabels(rects1)
autolabels(rects2)

# Show the plot
plt.show()
