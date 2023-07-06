import numpy as np

class AccessPoint:
    def __init__(self, id, position, frequency, power, bandwidth):
        self.id = id
        self.position = position
        self.frequency = frequency
        self.power = power
        self.bandwidth = bandwidth
        self.c = 299792458

    def getPosition(self):
        return self.position

    def info(self):
        return (self.id, self.position, self.frequency, self.power)

    def receivedPower(self, distance):
        L_dB = 20 * np.log10(self.frequency) + 20 * np.log10(distance) + 20 * np.log10(4 * np.pi / self.c) #La unidad del resultado es dB
        dB = self.power - 30                                                                               #Conversión de dBm a dB
        return dB - L_dB
    
    def SNR(self, distance, noise_power):
        signal_power = self.receivedPower(distance)
        return signal_power / noise_power
    
    def bitRate(self, distance, noise_power):
        SNR = self.SNR(distance, noise_power)
        return self.bandwidth * np.log2(1 + SNR)