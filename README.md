# Simulación de interferencia de señal ycalidad de servicio en redes WLAN

Integrantes:

1. Vicente Ignacio Carreño Escobar
2. Nicolás Andrés Ruiz Ruiz
3. Tabata Andrea Ahumada Avendaño

---

## Clases

### Area

Atributos:

1. width, determina el largo del área, su unidad es [m]
2. height, determina el ancho del área, su unidad es [m]

Funciones:

1. drawArea()

### AccessPoint

Atributos:

1. position, determina la posición espacial del access point, es una tupla conformada por (x, y), su unidad es [m].
2. frequency, determina la frecuencia de operación, su unidad es [Hz].
3. power, determina la potencia de transmisión del access point, su unidad es [dBm]

Funciones:

1. receivedPower(distance)