# 📊 Matplotlib Multiple Figures & Subplots 
# This program demonstrates how to create:
# 1. A figure with multiple subplots
# 2. Separate figures with different plots
# 3. Random plots in a loop

import matplotlib.pyplot as plt
import numpy as np

# ================================
# Figure 1: Contains two subplots
# ================================
plt.figure(1)  # Create Figure 1

# First subplot (2 rows, 1 column, position 1)
plt.subplot(211)
plt.plot([1, 2, 3])
plt.title('Easy as 1, 2, 3')

# Second subplot (2 rows, 1 column, position 2)
plt.subplot(212)
plt.plot([4, 5, 6])

# ================================
# Figure 2: A separate figure
# ================================
plt.figure(2)  # Create Figure 2
plt.plot([4, 5, 6])
plt.title("Figure 2 Plot")

# ================================
# Figure 3: Random plots
# ================================
plt.figure(3)  # Create Figure 3

# Plot 3 random lines
for i in range(3):
    plt.plot(np.random.rand(10))  

plt.title("Random Plots")

# ================================
# Show all figures
# ================================
plt.show()
