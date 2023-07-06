import matplotlib.pyplot as plt
import numpy as np

class AccessPoint:
    def __init__(self, frecuencia, ancho_banda, potencia_transmision):
        self.frecuencia = frecuencia
        self.ancho_banda = ancho_banda
        self.potencia_transmision = potencia_transmision

    def calcular_ganancia_antena(self, angulo):
        # Implementa aquí la lógica para calcular la ganancia de la antena en función del ángulo
        # Puedes usar fórmulas matemáticas o datos específicos de la antena

        # Por ejemplo, aquí se usa una función de ganancia constante para simplificar el ejemplo:
        return 10  # Ganancia constante de 10 dB

    def dibujar_diagrama_radiacion(self):
        angles = np.linspace(0, 2 * np.pi, 360)  # Ángulos en radianes
        gains = [self.calcular_ganancia_antena(angle) for angle in angles]

        # Convertir ganancia a escala lineal y aplicar potencia de transmisión
        gains_linear = 10 ** (np.array(gains) / 10)
        gains_linear *= self.potencia_transmision

        # Dibujar el diagrama de radiación
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
        ax.plot(angles, gains_linear)
        ax.set_rlabel_position(0)  # Posición de las etiquetas radiales

        plt.title('Diagrama de Radiación')
        plt.show()

# Ejemplo de uso
ap = AccessPoint(frecuencia=2.4, ancho_banda=20, potencia_transmision=20)
ap.dibujar_diagrama_radiacion()