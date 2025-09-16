# Plotting Line Graphs in Matplotlib with ggplot Style

from matplotlib import pyplot as plt 
import matplotlib.style as mplstyle

# Apply style before plotting
mplstyle.use('ggplot') 

x = [5, 8, 10]
y = [12, 16, 6]
x1 = [6, 9, 11]
y1 = [7, 15, 9]

plt.plot(x,y, marker='o') # For dot points
plt.plot(x1, y1, linewidth=5)

# Adding title and axis labels
plt.title("Epic info")
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Show the plot
plt.show()
