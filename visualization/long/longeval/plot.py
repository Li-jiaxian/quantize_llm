import os
import argparse
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# longchat_7b_16k = [0.942, 0.876, ,0.678 ,0.532, 0.444]
longchat_13b_16k = [0.97, 0.926, 0.908, 0.86, 0.766, 0.658]

x_plot = ['5k', '7k', '9k', '12k', '14k', '16k']

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(x_plot, longchat_13b_16k, marker='s', linestyle='-.', color='green', label='LongChat-13B-16K')

# Adding titles and labels
plt.xlabel('Context Length')
plt.ylabel('Accuracy')

# Customizing the plot to match the style
plt.ylim(0, 1.0)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Customizing the background
plt.gca().set_facecolor('#f5f5f5')

# Displaying the plot
plt.show()