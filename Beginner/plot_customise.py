# Life cylce of plot 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Sample company revenue data
data = {'Barton LLC': 109438.50,
        'Farmi, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling Ltd':100934.30,
        'Lopee Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows':123381.81,
        'White-Trantow':135841.99,
        'Will LLC': 104437.60}

group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

# -------------------------
# 1. Basic horizontal bar chart
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
plt.show()

# -------------------------
# 2. Rotate x-axis tick labels
plt.rcParams.update({'figure.autolayout': True})
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[10000,140000], xlabel='Total Revenue', ylabel='Company', title='Company Revenue')
plt.show()

# -------------------------
# 3. Specify figure size
plt.rcParams.update({'figure.autolayout': True})
fig, ax = plt.subplots(figsize=(8,4))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[10000,140000], xlabel='Total Revenue', ylabel='Company', title='Company Revenue')
plt.show()

# -------------------------
# 4. Apply custom currency formatter
def currency(x, pos):
    """Format axis ticks as currency in K (thousands) or M (millions)."""
    if x >= 1e6:
        s = '${:1.1f}M'.format(x*1e-6)
    else:
        s = '${:1.0f}K'.format(x*1e-3)
    return s

formatter = FuncFormatter(currency)

fig, ax = plt.subplots(figsize=(6,8))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[10000,140000], xlabel='Total Revenue', ylabel='Company', title='Company Revenue')
ax.xaxis.set_major_formatter(formatter)
plt.show()

# -------------------------
# 5. Advanced customization with mean line & annotations
fig, ax = plt.subplots(figsize=(8,8))
ax.barh(group_names, group_data)
plt.setp(labels, rotation=45, horizontalalignment='right')

# Add vertical line at the mean revenue
ax.axvline(group_mean, ls='--', color='r')

# Annotate some companies
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10, verticalalignment="center")

# Adjust title, ticks, and formatting
ax.title.set(y=1.05)
ax.set(xlim=[10000,140000], xlabel='Total Revenue', ylabel='Company', title='Company Revenue')
ax.xaxis.set_major_formatter(formatter)
ax.set_xticks([0,25e3,50e3,125e3])

# Adjust spacing
fig.subplots_adjust(right=0.8)
plt.show() 

# -------------------------
# 6. Save the final figure in disk
fig.savefig('sales.png',transparent=False, dpi=80, bbox_inches='tight')
