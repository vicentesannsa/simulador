import numpy as np

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