# Demonstration of 3D Scatter Plot, 2D Line/Scatter Plot, and Bar Charts in Matplotlib

import matplotlib.pyplot as plt

# ---------- 3D Scatter Plot ----------
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

# Sample data for X, Y, Z points
x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,2,3,13,4,1,2,4,8]
z = [2,3,3,3,5,7,9,11,9,10]

# Plot red scatter points in 3D
ax.scatter(x, y, z, c='r', marker='o')

# Axis labels
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')

plt.show()

# ---------- 2D Line and Scatter Plot ----------
fig=plt.figure()
ax=fig.add_subplot(111)

# Line plot
ax.plot([1,2,3,4], [10,20,25,30], color='lightblue', linewidth=3)

# Scatter plot with triangle markers
ax.scatter([0.3, 3.8, 1.2, 2.5],[11, 25, 9, 26], color='darkgreen', marker='^')

# Limit X-axis range
ax.set_xlim(0.5,4.5)
plt.show()

# ---------- Bar Charts (Side by Side) ----------
fig = plt.figure(figsize=(20,10))  # Wide figure for two subplots
ax1 = fig.add_subplot(121)  # Left subplot
ax2 = fig.add_subplot(122)  # Right subplot

# Vertical bar chart
ax1.bar([1,2,3], [3,4,5])

# Horizontal bar chart
ax2.barh([0.5,1,2.5], [0,1,2])

# Show the plot
plt.show()
