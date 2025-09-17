# Program: Visualization of Random and Structured Ellipses using Matplotlib

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# ------------------------------
# Figure 1: Randomized Ellipses
# ------------------------------
 # Number of ellipses to draw
NUM = 250  

# Create a list of random ellipses
ells = [
    Ellipse(
        xy=np.random.rand(2) * 10,   # Random (x, y) within 0–10
        width=np.random.rand(),      # Random width
        height=np.random.rand(),     # Random height
        angle=np.random.rand() * 360 # Random rotation angle
    )
    for i in range(NUM)
]

# Create figure with equal aspect ratio (so ellipses look correct)
fig, ax= plt.subplots(subplot_kw={'aspect':'equal'})

# Add ellipses to the plot with random styles
for e in ells:
    ax.add_artist(e)                      # Add ellipse to axes  
    e.set_clip_box(ax.bbox)               # Clip ellipse within plot area
    e.set_alpha(np.random.rand())         # Random transparency
    e.set_facecolor(np.random.rand(3))    # Random RGB color

# Set plot limits
ax.set_xlim(0,10)
ax.set_ylim(0, 10)
plt.show()

# ------------------------------
# Figure 2: Structured Ellipses
# ------------------------------
delta = 45.0
angles=np.arange(0, 360 + delta, delta)     # Angles from 0° to 360° in 45° steps

# Create ellipses centered at origin, rotated by different angles
ells = [Ellipse(xy=(0, 0), width=4, height=2, angle=a) for a in angles]

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

for e in ells:
    e.set_clip_box(ax.bbox)     # Keep ellipses inside plot area
    e.set_alpha(0.1)            # Low transparency for overlapping view
    ax.add_artist(e)            # Add ellipse to axes      

# Set axis limits to fully show ellipses
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
plt.show()
    