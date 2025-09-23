# Program Title: Advanced GridSpec and Subplot Layouts in Matplotlib
# Description: This program demonstrates multiple methods to create and manage complex subplot layouts
#              using Matplotlib's GridSpec. It covers constrained layouts, nested grids, variable row/column
#              ratios, and custom subplot arrangements, including creating a grid of small plots with clean spines.

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from itertools import product
import numpy as np

# -----------------------------
# Method 1: Simple 2x2 subplots using plt.subplots
# -----------------------------
fig1, f1_axes = plt.subplots(ncols=2, nrows=2, constrained_layout=True)
plt.show()

# -----------------------------
# Method 2: 2x2 subplots using GridSpec
# -----------------------------
fig2 = plt.figure(constrained_layout = True)
spec2 = gridspec.GridSpec(ncols = 2, nrows = 2, figure = fig2)
f2_ax1 = fig2.add_subplot(spec2[0,0])
f2_ax2 = fig2.add_subplot(spec2[0,1])
f2_ax3 = fig2.add_subplot(spec2[1,0])
f2_ax4 = fig2.add_subplot(spec2[1,1])
plt.show()

# -----------------------------
# Method 3: Advanced indexing of GridSpec
# -----------------------------
fig3 = plt.figure(constrained_layout = True)
gs = fig3.add_gridspec(3,3)

f3_ax1 =  fig3.add_subplot(gs[0, :])
f3_ax1.set_title('gs[0, :]')

f3_ax2 =  fig3.add_subplot(gs[1, :-1])
f3_ax2.set_title('gs[1, :-1]')

f3_ax3 =  fig3.add_subplot(gs[1:, -1])
f3_ax3.set_title('gs[1:, -1]')

f3_ax4 =  fig3.add_subplot(gs[-1, 0])
f3_ax4.set_title('gs[-1, 0]')

f3_ax5 =  fig3.add_subplot(gs[-1, -2])
f3_ax5.set_title('gs[-1, -2]')

plt.show()

# -----------------------------
# Method 4: Annotate subplots
# -----------------------------
fig4 = plt.figure(constrained_layout = True)
spec4 = fig4.add_gridspec(ncols= 2, nrows=2)
anno_opts =dict(xy = (0.5, 0.5), xycoords ='axes fraction', va ='center', ha = 'center')

f4_ax1 = fig4.add_subplot(spec4[0, 0])
f4_ax1.annotate('GridSpec[0, 0]', **anno_opts)

f4_ax2 = fig4.add_subplot(spec4[0, 1])
f4_ax2.annotate('GridSpec[0, 1]', **anno_opts)

f4_ax3 = fig4.add_subplot(spec4[1, 0])
f4_ax3.annotate('GridSpec[1, 0]', **anno_opts)

f4_ax4 = fig4.add_subplot(spec4[1, 1])
f4_ax4.annotate('GridSpec[1, 1]', **anno_opts)

plt.show()

# -----------------------------
# Method 5: Subplots with different width and height ratios
# -----------------------------
fig5 = plt.figure(constrained_layout = True)
widths = [2,3,1.5]
height = [1,3,2]
spec5 = fig5.add_gridspec(ncols=3, nrows=3, width_ratios = widths, height_ratios = height)
for row in range(3):
    for col in range(3):
        ax = fig5.add_subplot(spec5[row, col])
        label = 'width: {}\n Height:{}'.format(widths[col], height[row])
        ax.annotate(label, (0.1, 0.5), xycoords = 'axes fraction', va='center')

plt.show()

# -----------------------------
# Method 6: Using plt.subplots with width_ratios and height_ratios
# -----------------------------
gs_kw = dict(width_ratios = widths, height_ratios = height)
fig6, f6_axes = plt.subplots(ncols = 3, nrows=3, constrained_layout = True, gridspec_kw=gs_kw)
for r, row in enumerate(f6_axes):
    for c, ax in enumerate(row):
        label = 'width: {}\n Height:{}'.format(widths[c], height[r])
        ax.annotate(label, (0.1, 0.5), xycoords = 'axes fraction', va='center')
plt.show()

# -----------------------------
# Method 7: Create big subplot by removing smaller ones
# -----------------------------
fig7, f7_axes = plt.subplots(ncols = 3, nrows=3)
gs = f7_axes[1,2].get_gridspec()

# Remove smaller axes
for ax in f7_axes[1:, -1]:
    ax.remove()
    
# Add a big subplot spanning multiple grid cells
axbig = fig7.add_subplot(gs[1:, -1])
axbig.annotate('Big Axes \n Gridspec[1:, -1]', (0.1, 0.5), xycoords='axes fraction', va='center')
fig7.tight_layout()
plt.show()

# -----------------------------
# Method 8: Subplots with custom spacing
# -----------------------------
fig8 = plt.figure(constrained_layout = True)
gs1 = fig8.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48, wspace=0.05)
f8_ax1 = fig8.add_subplot(gs1[:-1, :])
f8_ax2 = fig8.add_subplot(gs1[-1, :-1])
f8_ax3 = fig8.add_subplot(gs1[-1, -1])
plt.show()

# -----------------------------
# Method 9: Two separate grids in one figure
# -----------------------------
fig9 = plt.figure(constrained_layout = True)
gs1 = fig9.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48, wspace=0.05)
f9_ax1 = fig9.add_subplot(gs1[:-1, :])
f9_ax2 = fig9.add_subplot(gs1[-1, :-1])
f9_ax3 = fig9.add_subplot(gs1[-1, -1])

gs2 = fig9.add_gridspec(nrows=3, ncols=3, left=0.55, right=0.98, wspace=0.05)
f9_ax4 = fig9.add_subplot(gs2[:-1, :])
f9_ax5 = fig9.add_subplot(gs2[-1, :-1])
f9_ax6 = fig9.add_subplot(gs2[-1, -1])

plt.show()

# -----------------------------
# Method 10: Nested subgrids
# ----------------------------
fig10 = plt.figure(constrained_layout = True)
gs0 = fig10.add_gridspec(1, 2)
gs00 = gs0[0].subgridspec(2,3)
gs01 = gs0[1].subgridspec(3,2)

for a in range(2):
    for b in range (3):
        fig10.add_subplot(gs00[a, b])

for a in range(3):
    for b in range (2):
        fig10.add_subplot(gs01[a, b])
plt.show()

# -----------------------------
# Method 11: Grid of small squiggle plots with cleaned spines
# -----------------------------
def squiggle_xy(a,b,c,d, i = np.arange(0.0, 2*np.pi, 0.05)):
    """Generates x and y coordinates for squiggle patterns"""
    return np.sin(i * a) * np.cos(i * b), np.sin(i * c) * np.cos(i * d)

fig11 = plt.figure(figsize=(8,8), constrained_layout = False)
outer_grid = fig11.add_gridspec(4, 4, wspace = 0.0, hspace = 0.0)

# Loop through 16 outer grid cells
for i in range(16):
    inner_grid = outer_grid[i].subgridspec(3, 3, wspace = 0.0, hspace = 0.0)
    a, b = i // 4 + 1, i % 4 + 1
    
    # Loop through inner 3x3 grid
    for j, (c,d) in enumerate(product(range(1,4), repeat=2)):
        ax = fig11.add_subplot(inner_grid[j])
        ax.plot(*squiggle_xy(a,b,c,d))
        ax.set_xticks([])
        ax.set_yticks([])
        # fig11.add_subplot(ax)

# Clean up spines for aesthetic
all_axes = fig11.get_axes()
for ax in all_axes:
    for sp in ax.spines.values():
        sp.set_visible(False)
     
    ss = ax.get_subplotspec()
    if ss.is_first_row():
        ax.spines['top'].set_visible(True)
    if ss.is_last_row():
        ax.spines['bottom'].set_visible(True)
    if ss.is_first_col():
        ax.spines['left'].set_visible(True) 
    if ss.is_last_col():
        ax.spines['right'].set_visible(True)

plt.show()
