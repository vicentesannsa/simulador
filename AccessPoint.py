import numpy as np

class AccessPoint:
    def __init__(self, position, frequency, power):
        self.position = position
        self.frequency = frequency
        self.power = power
        self.c = 299792458

    def receivedPower(self, distance):
        L_dB = 20 * np.log10(self.frequency) + 20 * np.log10(distance) + 20 * np.log10(4 * np.pi / self.c) #La unidad del resultado es dB
        dB = self.power - 30                                                                               #Conversión de dBm a dB
        return dB - L_dB
    
ap1_position = np.array([0, 0]) #m
ap1_frequency = 2.4e9           #Hz
ap1_power = 20                  #dBm

ap1 = AccessPoint(ap1_position, ap1_frequency, ap1_power)

distance = 35863e3
power_received = ap1.receivedPower(distance)

print(f"Potencia recibida en el punto a {distance} metros de distancia del AP1: {power_received} dB")