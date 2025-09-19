# Matplotlib Styling Demonstration – Using Styles, Contexts, and rcParams

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use('ggplot')

data = np.random.rand(50)
plt.show()

# ---- Using style context for temporary styling ----
x = np.linspace(0, 2*np.pi, 50)   # from 0 to 2π, 50 points
y = np.sin(x)                     # Compute sine values

with plt.style.context('dark_background'):
    plt.plot(y, 'ro-')       # Red circles with lines
plt.show()

# ---- Changing default style globally using rcParams ----
mpl.rcParams['lines.linewidth'] = 2   # Set default line width
mpl.rcParams['lines.color'] = 'r'     # Set default line color (red)

plt.plot(data)
plt.show()

# Dark lines
mpl.rc('lines', linewidth=4, color='r')    # Thick lines
plt.plot(data)
plt.show()
