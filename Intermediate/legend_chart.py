# Program Title: Advanced Legend Customization in Matplotlib
# Description: This program demonstrates various ways to create and customize legends in Matplotlib,
#              including using custom legend handlers for patches, lines, tuples, and even dummy objects.
#              It covers multiple legend techniques like bbox placement, multiple legends, HandlerLine2D,
#              HandlerTuple, HandlerPatch, and creating completely custom legend elements.

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerLine2D, HandlerBase, HandlerTuple, HandlerPatch
import matplotlib.patches as mpatches
from matplotlib.legend import Legend
from numpy.random import randn

# -----------------------------
# 1. Basic Patch Legend
# -----------------------------
red_patch = mpatches.Patch(color='red', label = 'The Red data')
plt.legend(handles = [red_patch])
plt.show()

# -----------------------------
# 2. Basic Line Legend
# -----------------------------
blue_line = mlines.Line2D([], [], color = 'blue', marker='*', markersize = 15, label = 'Blue Stars')
plt.legend(handles = [blue_line])
plt.show()

# -----------------------------
# 3. Legends with subplot and bbox_to_anchor
# -----------------------------
plt.subplot(211)
plt.plot([1,2,3], label="test1")
plt.plot([3,2,1], label='test2')
plt.legend(bbox_to_anchor =(0., 1.02, 1., .102), loc='lower left', ncols = 2, mode = "expand", borderaxespad = 0.)

plt.subplot(223)
plt.plot([1,2,3], label="test1")
plt.plot([3,2,1], label='test2')
plt.legend(bbox_to_anchor =(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()

# -----------------------------
# 4. Multiple legends on same axes
# -----------------------------
line1, = plt.plot([1,2,3], label = "line 1", linestyle = "--")
line2, = plt.plot([3,2,1], label ="line 2", linewidth = 4)
first_legend = plt.legend(handles = [line1], loc = 'upper right')
ax = plt.gca().add_artist(first_legend)
plt.legend(handles = [line2], loc = 'lower right')
plt.show()

# -----------------------------
# 5. Legend handler with custom number of points
# -----------------------------
line1, = plt.plot([1,2,3], marker='o', label = 'line 1')
line2, = plt.plot([3,2,1], marker='o', label ='line 2')
# Either use of them
# plt.legend(handler_map ={line1: HandlerLine2D(numpoints=4)}) 
plt.legend(handler_map = {type(line1): HandlerLine2D(numpoints=4)})
plt.show()

# -----------------------------
# 6. Tuple in legends
# -----------------------------
z = randn(10)
red_dot, = plt.plot(z, "ro", markersize = 15)
white_cross, = plt.plot(z[:5], "w+", markeredgewidth = 3, markersize = 15)
# Legend contains single object and a tuple of objects
plt.legend([red_dot, (red_dot, white_cross)], ["Attr A",  "Attr B"])
plt.show()

# -----------------------------
# 7. HandlerTuple example
# -----------------------------
p1, = plt.plot([1,2,5,3], 'r-d')
p2, = plt.plot([3,2,1], 'k-o')
l = plt.legend([(p1, p2)], ['Two keys'], numpoints = 1, handler_map = {tuple: HandlerTuple(ndivide=None)})
plt.show()

# -----------------------------
# 8. Custom handler with dummy object
# -----------------------------
# Dummy object that we want to appear in the legend
class AnyObject:
    pass

# Custom handler
class AnyObjectHandler(HandlerBase):
    """Custom legend handler for AnyObject"""
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        patch = mpatches.Rectangle(
            [xdescent, ydescent], width, height,
            facecolor='red', edgecolor='black', hatch='xx', lw=3,
            transform=trans
        )
        return [patch]

# Use custom handler in legend
plt.legend([AnyObject()], ['My first Handler'], handler_map={AnyObject: AnyObjectHandler()})
plt.show()

# -----------------------------
# 9. Custom Patch handler example
# -----------------------------
class HandlerEllispe(HandlerPatch):
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        center = 0.5 * width - 0.5 * xdescent, 0.5 * height - 0.5 * ydescent
        p = mpatches.Ellipse( xy=(center[0] + xdescent, center[1] + ydescent),
                    width=width, height=height)
        self.update_prop(p, orig_handle, legend) # Inherit properties
        p.set_transform(trans)
        return [p]

# Add a patch and use custom handler in legend
c = mpatches.Circle((0.5, 0.5), 0.25, facecolor = "green", edgecolor = "red", lw=2)
plt.gca().add_patch(c)
plt.legend([c], ["An ellipse not a rectangle"], handler_map = {mpatches.Circle: HandlerEllispe()})
plt.show()
