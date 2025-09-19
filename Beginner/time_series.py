# Program: Time Series Plot with Custom Date Formatting using Matplotlib

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# Create dummy time series data
dates = np.arange('2015-01', '2021-01', dtype='datetime64[M]')
prices = np.linspace(500, 1500, len(dates)) + np.random.randn(len(dates)) * 50

# Formatters/Locators. Define major and minor tick locators for X-axis (time axis)
years = mdates.YearLocator() # major ticks each year
months = mdates.MonthLocator() # minor ticks each month
yearsFmt = mdates.DateFormatter('%Y')

fig, ax = plt.subplots()
ax.plot(dates, prices)

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

# Set X-axis limits
datemin = np.datetime64(dates[0], 'Y')
datemax = np.datetime64(dates[-1], 'Y') + np.timedelta64(1, 'Y')
ax.set_xlim(datemin, datemax)

# Format y-axis values
def price(x):
    return '$%.2f' % x

# Set data formatters for better interactivity (hover/zoom)
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = price

# Add grid and auto-format date labels
ax.grid(True)
fig.autofmt_xdate()
plt.show()
