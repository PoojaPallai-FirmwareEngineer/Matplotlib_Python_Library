# Program: Drawing Figure-Level Diagonal Lines using Matplotlib’s Line2D

import matplotlib.pyplot as plt
import matplotlib.lines as lines

# Use ggplot style
plt.style.use('ggplot')

fig = plt.figure()

# Create two lines across the figure
l1 = lines.Line2D([0,1], [0,1],transform = fig.transFigure, figure=fig)
l2 = lines.Line2D([0,1], [1,0],transform = fig.transFigure, figure=fig)

# Add them to the figure
fig.lines.extend([l1, l2])

plt.show()
