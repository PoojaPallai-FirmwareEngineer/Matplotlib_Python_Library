# Program: Real-Time Sine Wave Visualization Using Sliders, Buttons, and Radio Controls

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons

# -----------------------------
# 1. Create figure and axes
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

# -----------------------------
# 2. Generate initial sine wave data
t = np.arange(0.0, 1.0, 0.001)  # Time values
a0 = 5                           # Initial amplitude
f0 = 3                           # Initial frequency
delta_f = 5.0                     # Frequency step for slider
s = a0 * np.sin(2 * np.pi * f0 * t)
l, = plt.plot(t, s, lw=2, color='red')  # Plot sine wave
plt.axis([0, 1, -10, 10])                # Set axis limits

# -----------------------------
# 3. Create sliders for frequency and amplitude
axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0, valstep=delta_f)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)

# Update sine wave when slider values change
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()

sfreq.on_changed(update)
samp.on_changed(update)

# -----------------------------
# 4. Reset button to restore initial values
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()

button.on_clicked(reset)

# -----------------------------
# 5. Radio buttons to change line color
rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)

def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
    
radio.on_clicked(colorfunc)

# 6. Show the plot
plt.show()
