# Matplotlib Streamplot Demonstration – Density, Color, Linewidth, Start Points, and Masking

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 -X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U*U + V*V)

fig = plt.figure(figsize=(7, 9))
gs = gridspec.GridSpec(3, 2, height_ratios=[1,1,2])

# ---- First subplot: density variation ----
ax0 = fig.add_subplot(gs[0,0])
ax0.streamplot(X, Y, U, V, density=[0.5, 1])
ax0.set_title('Varying Density')

# ---- Second subplot: varying color ----
ax1 = fig.add_subplot(gs[0, 1])
strm = ax1.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
fig.colorbar(strm.lines)
ax1.set_title("Varying Color")

# ---- Third subplot: varying linewidth ----
ax2 = fig.add_subplot(gs[1, 0])
lw = 5*speed / speed.max()
strm = ax2.streamplot(X, Y, U, V, color='k', linewidth=lw)
ax2.set_title("Varying Line width")

# ---- Fourth subplot: controlling start points ----
seed_points = np.array([[-2, -1, 0, 1, 2, -1], [-2, -1, 0, 0, 2, 2]])
ax3 = fig.add_subplot(gs[1, 1])
strm = ax1.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn', start_points=seed_points.T)
fig.colorbar(strm.lines)
ax3.set_title("Controlling starting Points")
ax3.plot(seed_points[0], seed_points[1], 'bo')
ax3.axis((-w, w, -w, w))

# ---- Fifth subplot: masking ----
mask=np.zeros(U.shape, dtype=bool)
mask[40:60, 40:60] = True
U = np.ma.array(U, mask=mask)
ax4 = fig.add_subplot(gs[2:,:])
ax4.streamplot(X, Y, U, V, color='r')
ax4.set_title("Streamplot with masking")
ax4.imshow(~mask, extent=(-w, w, -w, w), alpha=0.5, interpolation='nearest', cmap='gray', aspect='auto') 
ax4.set_aspect('equal')

plt.tight_layout()   # Automatically adjusts subplot spacing to prevent overlap of titles, labels, and colorbars
plt.show()
