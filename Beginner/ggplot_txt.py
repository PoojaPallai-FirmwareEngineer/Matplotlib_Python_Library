# Program to Plot Graph from Text File Data using Matplotlib and ggplot Style using numpy

import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
import numpy as np

mplstyle.use("ggplot")

x,y = np.loadtxt('loadfile.txt', unpack=True, delimiter=',')
plt.plot(x, y, marker='o')
plt.title("Epic info")
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True, color='k')
plt.show()
