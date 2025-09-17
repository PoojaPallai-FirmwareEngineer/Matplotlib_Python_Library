# Program: Matplotlib Demonstration: Bar Charts and Filled Area Plots

import matplotlib.pyplot as plt
import numpy as np

# Reset matplotlib settings to defaults
plt.rcdefaults()

# ----------------------------------------------------
# Part 1: Horizontal Bar Chart with Error Bars
# ----------------------------------------------------
fig, ax = plt.subplots()
people = ('Tom', 'Dick', 'Harry', 'Slim')

# Create positions for y-axis
y_pos = np.arange(len(people))  

# Generate random performance values
performance = 3 + 10 * np.random.rand(len(people))

# Generate random error values for each bar
error = np.random.rand(len(people))

# Plot horizontal bar chart with error bars
ax.barh(y_pos, performance, xerr=error, align='center', color='green', ecolor='black')

# Set y-axis ticks and labels
ax.set_yticks(y_pos)
ax.set_yticklabels(people)

# Invert y-axis so the first person appears at the top
ax.invert_yaxis()

# Set axis label and chart title
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# Display the first figure
plt.show()

# ----------------------------------------------------
# Part 2: Damped Sine Wave with Filled Area
# ----------------------------------------------------
# Generate X values (0 to 1)
x = np.linspace(0, 1, 500)

# Define damped sine function
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

# Create new figure
fig, ax = plt.subplots()

# Fill the area under the curve
ax.fill(x, y, zorder=10)

# Add grid lines below the filled plot
ax.grid(True, zorder=5)

# Display the second figure
plt.show()

# ----------------------------------------------------
# Part 3: Overlapping Sine Waves with Transparency
# ----------------------------------------------------
# Generate X values (0 to 2π)
x = np.linspace(0, 2 * np.pi, 500)

# Define two sine waves
y1 = np.sin(x)
y2 = np.sin(3 * x)

# Create new figure
fig, ax = plt.subplots()

# Fill areas under both sine waves with transparency
ax.fill(x, y1, 'b', x, y2, 'r', alpha=0.3)

# Display the third figure
plt.show()
