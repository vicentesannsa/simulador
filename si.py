import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from scipy.constants import Boltzmann

class User:
    def __init__(self, id, position, step_size=1.5):
        self.id = id
        self.position = position
        self.step_size = step_size
        self.direction = np.random.uniform(0, 2*np.pi)

    def move(self, width, height):
        dx = self.step_size * np.cos(self.direction)
        dy = self.step_size * np.sin(self.direction)

        new_position = self.position + np.array([dx, dy])

        if new_position[0] < 0 or new_position[0] > width:
            self.direction = np.pi - self.direction
        elif new_position[1] < 0 or new_position[1] > height:
            self.direction = -self.direction

        dx = self.step_size * np.cos(self.direction)
        dy = self.step_size * np.sin(self.direction)

        self.position = self.position + np.array([dx, dy])

    def info(self):
        return (self.id, self.position)


class Area:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fig, self.ax = plt.subplots()

    def addUsers(self, users):
        self.user_plots = []
        for user in users:
            plot, = self.ax.plot(*user.position, 'bo')
            self.user_plots.append(plot)

    def addAccessPoints(self, aps):
        for ap in aps:
            self.ax.plot(*ap.position, 'ro')

    def drawArea(self):
        rect = patches.Rectangle((0, 0), self.width, self.height, edgecolor='red', facecolor='none')
        self.ax.add_patch(rect)
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)


class AccessPoint:
    def __init__(self, id, position, frequency, power, bandwidth):
        self.id = id
        self.position = position
        self.frequency = frequency
        self.power = power  # dBm
        self.bandwidth = bandwidth  # Hz
        self.c = 299792458

    def info(self):
        return (self.id, self.position, self.frequency, self.power)

    def receivedPower(self, distance):
        L_dB = 20 * np.log10(self.frequency) + 20 * np.log10(distance) + 20 * np.log10(4 * np.pi / self.c)
        dB = self.power - 30
        return dB - L_dB

    def SNR(self, distance, noise_power):
        signal_power = self.receivedPower(distance)
        return signal_power / noise_power

    def bitRate(self, distance, noise_power):
        snr = self.SNR(distance, noise_power)
        return self.bandwidth * np.log2(1 + snr)  # Shannon's theorem


class Simulator:
    def __init__(self, width, height, AP, AP_config, users, noise_power):
        self.width = width
        self.height = height
        self.AP = AP
        self.AP_config = AP_config
        self.users = users
        self.noise_power = noise_power
        self.area = Area(self.width, self.height)

        self.AP_list = []
        for i in range(self.AP):
            position = self.AP_config.pop(0)
            frequency = self.AP_config.pop(0)
            power = self.AP_config.pop(0)
            bandwidth = self.AP_config.pop(0)
            self.AP_list.append(AccessPoint(i, position, frequency, power, bandwidth))

        self.area.addUsers(self.users)
        self.area.addAccessPoints(self.AP_list)

        for user in self.users:
            for AP in self.AP_list:
                distance = np.linalg.norm(AP.position - user.position)
                print(f"User {user.id} is connected to AP {AP.id} with bit rate {AP.bitRate(distance, self.noise_power)} bps")

    def accessPoint(self):
        for AP in self.AP_list:
            print(AP.info())

    def update(self, frame):
        for user, plot in zip(self.users, self.area.user_plots):
            user.move(self.width, self.height)
            plot.set_data(*user.position)

    def startSimulator(self):
        self.accessPoint()
        self.area.drawArea()
        self.anim = FuncAnimation(self.area.fig, self.update, frames=range(100), interval=200, repeat=False)
        plt.show()


users = [User(i, np.array([np.random.uniform(30, 50), np.random.uniform(30, 50)])) for i in range(50)]
AP_config = [np.array([1,1]), 2.4e9, 20, 20e6, np.array([11,11]), 5e9, 20, 20e6]

noise_power = -100  # dBm

simulator = Simulator(80, 50, 2, AP_config, users, noise_power)
simulator.startSimulator()