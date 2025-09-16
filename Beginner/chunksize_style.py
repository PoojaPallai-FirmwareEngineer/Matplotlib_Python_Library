"""
Program Title: Demonstration of Matplotlib Styles and Path Simplification

Description:
This program demonstrates the use of different Matplotlib styles 
and how path simplification & chunk size settings affect plot rendering performance.
It covers:
1. Path simplification with 'path.simplify_threshold'
2. Chunked rendering using 'agg.path.chunksize'
3. Using built-in styles like:
   - 'fast'
   - 'dark_background'
   - 'ggplot'
"""

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib as mpl
import matplotlib.style as mplstyle

mpl.rcParams['path.simplify_threshold'] = 1.0
y = np.random.rand(100000)
y[50000:] *= 2
y[np.logspace(1, np.log10(50000), 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True
mpl.rcParams['agg.path.chunksize'] = 0
plt.plot(y)
plt.show()
mpl.rcParams['agg.path.chunksize'] = 10000
plt.plot(y)
plt.show()

# Use fast style
mplstyle.use('fast')
plt.plot(y)
plt.title("Fast style")
plt.show()

# Use dark background
mplstyle.use('dark_background')
plt.plot(y)
plt.title("dark background style")
plt.show()

# Use ggplot
mplstyle.use('ggplot')
plt.plot(y)
plt.title("GGPlot style")
plt.show()
