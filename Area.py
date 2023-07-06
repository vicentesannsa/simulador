import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Area:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def drawArea(self):
        fig, ax = plt.subplots()

        #Crear el rectángulo
        rect = patches.Rectangle((self.x, self.y), self.width, self.height, edgecolor='red', facecolor='white', alpha=0.5)

        #Agregar el rectángulo al gráfico
        ax.add_patch(rect)

        #Personalizar el gráfico
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_aspect('equal')

        # Mostrar el gráfico
        plt.show()

area = Area(80, 50, 0, 0)
area.drawArea()