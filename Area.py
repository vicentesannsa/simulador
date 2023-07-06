import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Area:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def drawArea(self, AP_positions):
        fig, ax = plt.subplots()

        #Crear el rectángulo
        rect = patches.Rectangle((0, 0), self.width, self.height, edgecolor='red', facecolor='white', alpha=0.5)

        #Agregar el rectángulo al gráfico
        ax.add_patch(rect)

        for AP in AP_positions:
            coordinates = AP.getPosition()
            ax.scatter(coordinates[0], coordinates[1], color='blue')

        #Personalizar el gráfico
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_aspect('equal')

        # Mostrar el gráfico
        plt.show()