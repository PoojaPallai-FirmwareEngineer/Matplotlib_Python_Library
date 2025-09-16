# Program: Pie Chart Demonstration using Matplotlib

import matplotlib.pyplot as plt

# Labels for each slice
labels = 'Frogs', 'Hogs', 'Dogs', 'logs'

# Numerical/Percentage values for slices
sizes = [15, 30, 45, 10]

# 'explode' separates a slice from the rest (only 2nd slice here)
explode = (0, 0.1, 0, 0)

# Create a figure and an axis
fig1, ax1 = plt.subplots()

# Create the pie chart with various customizations
ax1.pie(
    sizes, 
    explode=explode,          # Highlight a slice
    labels=labels,            # Show category names
    autopct='%1.1f%%',        # Display percentage with 1 decimal
    shadow=True,              # Add shadow effect
    startangle=90             # Rotate start so first slice starts at 90°
)

# Equal aspect ratio ensures pie chart is circular
ax1.axis('equal')

plt.show()
