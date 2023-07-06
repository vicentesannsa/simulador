import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Area:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fig, self.ax = plt.subplots()

    def drawAP(self, AP_positions):
        for AP in AP_positions:
            coordinates = AP.getPosition()
            radius = 20
            theta = np.linspace(0, 2*np.pi, 100)
            x = coordinates[0] + radius * np.cos(theta)
            y = coordinates[1] + radius * np.sin(theta)

            self.ax.plot(x, y, color="black")
            self.ax.set_aspect('equal')
            self.ax.scatter(coordinates[0], coordinates[1], color='black')

    def drawArea(self):
        rect = patches.Rectangle((0, 0), self.width, self.height, edgecolor='red', facecolor='white', alpha=0.5)
        self.ax.add_patch(rect)
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)

    def drawUsers(self, users):
        self.user_plots = []
        for user in users:
            plot, = self.ax.plot(*user.position, 'bo')
            self.user_plots.append(plot)

    def showArea(self):
        plt.show()