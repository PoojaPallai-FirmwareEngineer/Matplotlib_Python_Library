"""
Program Title: Demonstration of Different Plot Types in Matplotlib

Description:
This program demonstrates several types of plots and scales using Matplotlib:
1. Line plots with different y-axis scales (linear, log, symlog, logit)
2. Scatter plot with varying colors and sizes
3. Categorical plotting (bar, scatter, line)
4. Histogram with normal distribution
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

# ----------------------------
# Generate data for line plots
# ----------------------------
np.random.seed(19680801)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))           # Sequential x values
plt.figure(1)

# Linear figure
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# Log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

# Symlog
plt.subplot(223)
plt.plot(x, y -y.mean())
plt.yscale('symlog', linthresh=0.01) # note: in newer matplotlib, use "linthresh" not "linthreshy"
plt.title('symlog')
plt.grid(True)

# Logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
plt.gca().yaxis.set_minor_formatter(NullFormatter())

# Adjust subplot spacing
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
plt.show()

# ----------------------------
# Scatter plot with size & color mapping
# ----------------------------
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),              # Colors
        'd': np.random.randn(50)}                       # Sizes
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.title("Scatter Plot with Variable Color and Size")
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

# ----------------------------
# Categorical plotting
# ----------------------------
names=['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.figure(1, figsize=(9,3))
plt.subplot(131)
plt.bar(names, values)

plt.subplot(132)
plt.scatter(names, values)

plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical plotting')
plt.show()

# ----------------------------
# Histogram (Normal Distribution)
# ----------------------------
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(100000)
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Proability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
