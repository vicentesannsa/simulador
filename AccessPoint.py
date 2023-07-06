import numpy as np

class AccessPoint:
    def __init__(self, id, position, frequency, power):
        self.id = id
        self.position = position
        self.frequency = frequency
        self.power = power
        self.c = 299792458

    def info(self):
        return (self.id, self.position, self.frequency, self.power)

    def receivedPower(self, distance):
        L_dB = 20 * np.log10(self.frequency) + 20 * np.log10(distance) + 20 * np.log10(4 * np.pi / self.c) #La unidad del resultado es dB
        dB = self.power - 30                                                                               #Conversión de dBm a dB
        return dB - L_dB