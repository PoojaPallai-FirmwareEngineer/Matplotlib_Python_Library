# Program: 2D Visualization with Pcolormesh and Contourf using Levels

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

# Step 1: Define grid spacing
dx, dy = 0.05, 0.05

# Step 2: Create grid coordinates (x, y)
# np.mgrid generates a 2D mesh
y, x = np.mgrid[slice(1, 5 + dy, dy), slice(1, 5 + dx,dx)]

# Step 3: Define z-values based on a mathematical function
z = np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)

# Step 4: Remove the last row and column to align array dimensions
z = z[:-1, :-1]

# Step 5: Define contour levels automatically (15 bins)
levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())

# Step 6: Choose a colormap and normalization for the levels
cmap = plt.get_cmap('PiYG')      # PiYG is a diverging colormap
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

# Step 7: Create two subplots (2 rows)
fig, (ax0, ax1) = plt.subplots(nrows=2)

# --- Plot 1: Pseudocolor plot using pcolormesh ---
im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
fig.colorbar(im, ax=ax0)
ax0.set_title('pcolormesh with levels')

# --- Plot 2: Filled contour plot using contourf ---
cf = ax1.contourf(x[:-1, : -1] + dx/2., y[:-1, : -1] + dx/2. , z, levels=levels, cmap=cmap)
fig.colorbar(cf, ax=ax1)
ax1.set_title('Contourf with levels')

# Step 8: Adjust layout for better spacing
fig.tight_layout()

# Step 9: Display the plot
plt.show()
