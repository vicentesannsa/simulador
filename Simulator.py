from Area import Area

class Simulator:
    def __init__(self, width, height, AP):
        self.width = width
        self.height = height
        self.AP = AP
        self.area = Area(self.width, self.height)

    def startSimulator(self):
        self.area.drawArea()

simulator = Simulator(80, 50, 2)
simulator.startSimulator()