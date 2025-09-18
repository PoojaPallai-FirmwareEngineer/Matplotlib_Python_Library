# Program: Visualizing Disaster Losses with Stacked Bars and Data Table"

import matplotlib.pyplot as plt
import numpy as np

# Disaster loss data (rows = years, columns = disaster types)
data = [[66386, 174296, 75131, 577908, 320151],
        [58230, 381139, 78045, 99308, 160454],
        [89135, 80552, 152558, 497981, 6063535],
        [78415, 81858, 150656, 193263, 69636],
        [139361, 331509, 343164, 781380, 52269]]

columns = ('Freeze', 'wind', 'flood', 'Quake', 'Hail')
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]

# Y-axis settings
values = np.arange(0, 2500, 500)        # scale steps for y-axis
value_increment = 1000                  # multiplier for y-axis values

# Define colors for rows using a colormap
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
n_rows = len(data)

# Bar chart positioning
index = np.arange(len(columns)) + 0.3
bar_width = 0.4

# Initialize y-offset for stacked bars
y_offset = np.zeros(len(columns))
cell_text = []

# ---- Plot stacked bars ----
for row in range(n_rows):
    # Draw bars for this row stacked on top of previous
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    
    # Update offset for stacking
    y_offset = y_offset + data[row]
    
    # Add cumulative values (scaled in 1000s) to display in the table
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])

# Reverse colors and text for table
colors = colors[::-1]
cell_text.reverse()

# Add table
the_table = plt.table(cellText=cell_text, rowLabels=rows, rowColours=colors, colLabels=columns, loc='bottom')

plt.subplots_adjust(left=0.2, bottom=0.2)
plt.ylabel("Loss in ${0}'s".format(value_increment))
plt.yticks(values * value_increment,['%d' % val for val in values])
plt.xticks([])      # Remove x-axis ticks
plt.title('Loss by disaster')
plt.show()
