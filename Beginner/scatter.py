# Program: Plotting Two Graphs with Matplotlib using Legends and ggplot Style

import matplotlib.pyplot as plt
import matplotlib.style as mplstyle

mplstyle.use("ggplot")

# First dataset
x = [5, 8, 10]
y = [12, 16, 6]

# Second dataset
x1 = [6, 9, 11]
y1 = [6, 15, 7]

# Scatter plots
plt.scatter(x, y, label="Dataset1")
plt.scatter(x1, y1, label="Dataset2")

# Adding title and axis labels
plt.title("Epic info")
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Legend (shows which points belong to which dataset)
plt.legend()

# Grid with black lines
plt.grid(True, color='k')

# Show the plt
plt.show()

