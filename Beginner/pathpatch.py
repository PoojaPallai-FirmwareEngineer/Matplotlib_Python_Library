# Program: Drawing Custom Shapes with Matplotlib Path and Patches

import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches

# Create a figure and axes
fig,ax = plt.subplots()

# Define shorthand for path
Path = mpath.Path

# Define path dath as sequence of drawing commands and points
path_data = [(Path.MOVETO, (1.58,-2.57)),            # Move to starting point
             (Path.CURVE4, (0.35, -1.1)),            # Cubic Bezier curve control point
             (Path.CURVE4, (-1.75, 2.0)),            # Second control point
             (Path.CURVE4, (0.375, 2.0)),            # End point of curve
             (Path.LINETO, (0.85, 1.15)),            # Draw a straight line
             (Path.CURVE4, (2.2, 3.2)),              # Start of another Bezier curve
             (Path.CURVE4, (3, 0.05)),               # Control point
             (Path.CURVE4, (2.0, -0.5)),             # End point of curve
             (Path.CLOSEPOLY, (1.58, -2.57))]        # Close the shape back to the start

# Separate codes and vertices from path data
codes, verts = zip(*path_data)

# Create Path object
path = mpath.Path(verts, codes)

# Create a PathPatch (the actual shape to display)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)

# Add patch to the axes
ax.add_patch(patch)

# Extract x and y coordinates of vertices for plotting
x, y = zip(*path.vertices)

# Plot vertices as green dots connected with lines
line, = ax.plot(x, y, 'go-')

# Add coordinate labels next to each vertex
for (x_val, y_val) in zip(x, y):
    ax.text(x_val + 0.1, y_val + 0.1, f"({x_val:.2f}, {y_val:.2f})",
            fontsize=8, color='blue')

# Add grid and set equal aspect ratio for proper shape visualization
ax.grid()
ax.axis('equal')

# Show the plot
plt.show()
