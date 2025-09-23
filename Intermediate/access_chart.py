# Program Title: Customizing Figure and Axes Appearance in Matplotlib
# Description: This program demonstrates how to access and modify figure and axes patches,
#              as well as customize the tick labels' color, rotation, and font size using Matplotlib.

import matplotlib.pyplot as plt

# Create a figure
fig = plt.figure()

# Access the figure patch (background) and set its color
rect = fig.patch
rect.set_facecolor('lightgoldenrodyellow') # Set figure background color

# Add axes to the figure
ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])  # [left, bottom, width, height]

# Access the axes patch (background of the axes) and set its color
rect = ax1.patch
rect.set_facecolor('lightslategray') # Set axes background color

# Customize x-axis tick labels
for label in ax1.xaxis.get_ticklabels():
    label.set_color("red")
    label.set_rotation(45)
    label.set_fontsize(12)

# Customize y-axis tick labels
for lines in ax1.yaxis.get_ticklabels():
    lines.set_color("green")
    lines.set_fontsize(12)

# Display the plot
plt.show()
