import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patches as patches


class graphFunctions(FigureCanvas):
    def __init__(self, parent=None):
        plt.style.use('dark_backgroud')
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
     
    def plot_gradient_bar(self):
        value = 70
        max_value = 100

        fig, ax = plt.subplots(figsize=(2, 6))

        # Create vertical gradient for full bar (height=1)
        gradient = np.linspace(0, 1, 256).reshape(256, 1)
        cmap = LinearSegmentedColormap.from_list('my_gradient', ['blue', 'red'])

        # Show gradient bar with fixed height 1 (full size)
        ax.imshow(gradient, aspect='auto', cmap=cmap, extent=(0, 1, 0, 1))

        # Draw border rectangle for the bar
        rect = patches.Rectangle((0, 0), 1, 1, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)

        # Calculate arrow Y position proportional to value
        arrow_y = value / max_value

        # Draw arrow on top of the bar at arrow_y
        ax.annotate('', xy=(0.5, arrow_y + 0.03), xytext=(0.5, arrow_y),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=4, headwidth=12))

        # Optional: show value text near arrow
        ax.text(0.5, arrow_y + 0.05, f'{value}', ha='center', va='bottom', fontsize=12)

        # Adjust axes
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.2)
        ax.axis('off')

        plt.show()