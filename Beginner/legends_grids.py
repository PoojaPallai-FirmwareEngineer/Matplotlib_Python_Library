# Program: Plotting Two Line Graphs in Matplotlib with ggplot Style and Legends

import matplotlib.pyplot as plt
import matplotlib.style as mplstyle

mplstyle.use("ggplot")

x = [5, 8, 10]
y = [12, 16, 6]
x1 = [6, 9, 11]
y1 = [6, 15, 7]

plt.plot(x, y, 'g', label='line one', linewidth=5)
plt.plot(x1, y1, 'c', label='line two', linewidth=3)

# Adding title and axis labels, legends
plt.title("Epic info")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()

# Grid with black lines
plt.grid(True, color='k')

# Show the plot
plt.show()
