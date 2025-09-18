"""
Program Title: Matplotlib Demo - Heatmap, Polygon Clipping, and Image Display

Description:
This program demonstrates:
1. Creating 2D Gaussian difference heatmaps
2. Displaying an image normally
3. Clipping an image using a polygon path
4. Loading and displaying an external image with fallback
"""

import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from pathlib import Path 
from matplotlib.path import Path as mpath # Matplotlib Path
import numpy as np
import os

# Optional fallback for sample images
try:
    from scipy.datasets import face
except ImportError:
    face = None  # Will handle later if SciPy is not installed

# ---------------------------
# Generate 2D Gaussian difference heatmap
# ---------------------------
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x,y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X-1)**2 - (Y-1)**2)
z = (Z1 - Z2) * 2
fig, ax = plt.subplots()
im = ax.imshow(z, interpolation='bilinear', cmap="RdYlGn", origin='lower', extent=[-3, 3, -3, 3], vmax = abs(z).max(), vmin = -abs(z).max())
plt.show()

# Define a polygon path (triangle)
vertices = [
    (0, 1),    # top
    (1, 0),    # right
    (0, -1),   # bottom
    (-1, 0),   # left
    (0, 1)     # back to top (close)
]
codes = [
    mpath.MOVETO,
    mpath.LINETO,
    mpath.LINETO,
    mpath.LINETO,
    mpath.CLOSEPOLY
]
clip_path = mpath(vertices, codes)
patch = PathPatch(clip_path, facecolor="none")

# ---------------------------
# Display clipped heatmap
# ---------------------------
fig, ax = plt.subplots()
ax.add_patch(patch)
im = ax.imshow(
    z, interpolation="bilinear", cmap="RdYlGn",
    origin="lower", extent=[-3, 3, -3, 3],
    vmax=abs(z).max(), vmin=-abs(z).max()
)
im.set_clip_path(patch)
plt.title("Clipped Image within Polygon Path")
plt.show()

# ---------------------------
# Step 5: Load and display an external image
# ---------------------------
# Option 1: Local image (watch.jpg)
image_path = Path(__file__).parent / "watch.jpg"

if os.path.exists(image_path):
    image = plt.imread(image_path)
else:
    # Option 2: Fallback to sample image from Scipy
    if face is not None:
        image = face()
    else:
        raise FileNotFoundError(
            "watch.jpg not found and SciPy sample image not available. "
            "Please place an image named 'watch.jpg' in the script folder."
        )
fig, ax = plt.subplots()
ax.imshow(image)
ax.axis('off')
plt.title("External Image Display")
plt.show()

