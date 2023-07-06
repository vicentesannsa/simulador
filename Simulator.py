import numpy as np
from AccessPoint import AccessPoint
from Area import Area

class Simulator:
    def __init__(self, width, height, AP, AP_config):
        self.width = width
        self.height = height
        self.AP = AP
        self.AP_config = AP_config
        self.area = Area(self.width, self.height)

        self.AP_list = []

        for i in range(self.AP):
            position = self.AP_config.pop(0)
            frequency = self.AP_config.pop(0)
            power = self.AP_config.pop(0)

            self.AP_list.append(AccessPoint(i, position, frequency, power))

    def accessPoint(self):
        for AP in self.AP_list:
            print(AP.info())

    def startSimulator(self):
        self.accessPoint()
        self.area.drawArea(self.AP_list)

AP_config = [np.array([1,1]), 2.4e9, 20, np.array([11,11]), 5e9, 20]

simulator = Simulator(80, 50, 2, AP_config)
simulator.startSimulator()

""" ap1_position = np.array([0, 0]) #m
ap1_frequency = 2.4e9           #Hz
ap1_power = 20                  #dBm

ap1 = AccessPoint(1, ap1_position, ap1_frequency, ap1_power)

distance = 35863e3
power_received = ap1.receivedPower(distance)

print(f"Potencia recibida en el punto a {distance} metros de distancia del AP1: {power_received} dB") """