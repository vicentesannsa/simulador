import numpy as np
from matplotlib.animation import FuncAnimation
from AccessPoint import AccessPoint
from Area import Area
from User import User

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

        self.area.drawArea()
        self.area.drawAP(self.AP_list)
        self.area.drawUsers(self.users)

        for user in self.users:
            for AP in self.AP_list:
                distance = np.linalg.norm(AP.position - user.position)
                print(f"User {user.id} is connected to AP {AP.id} with bit rate {AP.bitRate(distance, self.noise_power)} bps")

    def infoAP(self):
        for AP in self.AP_list:
            print(AP.info())

    def startSimulator(self):
        self.infoAP()
        self.anim = FuncAnimation(self.area.fig, self.update, frames=range(100), interval=200, repeat=False)
        self.area.showArea()
    
    def update(self, frame):
        for user, plot in zip(self.users, self.area.user_plots):
            user.move(self.width, self.height)
            plot.set_data(*user.position)

AP_config = [np.array([40,20]), 2.4e9, 20, 20e6, np.array([11,11]), 5e9, 20, 20e6, np.array([60,40]), 2.4e9, 20, 20e6]
noise_power = -100
users = [User(i, np.array([np.random.uniform(30, 50), np.random.uniform(30, 50)])) for i in range(50)]

simulator = Simulator(80, 50, 3, AP_config, users, noise_power)
simulator.startSimulator()