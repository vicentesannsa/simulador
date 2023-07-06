# Simulación de interferencia de señal y calidad de servicio en redes WLAN

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

1. id, determina el identificador del access point
2. position, determina la posición espacial del access point, es una tupla conformada por (x, y), su unidad es [m].
3. frequency, determina la frecuencia de operación, su unidad es [Hz].
4. power, determina la potencia de transmisión del access point, su unidad es [dBm]

Versión 2:


Este código implementa una simulación de un sistema de red inalámbrica con usuarios que se mueven en un área determinada. Aquí está la descripción de cada clase y función:

- `User`: Representa un usuario en la red. Cada usuario tiene un identificador (`id`), una posición (`position`) y un tamaño de paso (`step_size`). El método `move` se encarga de mover al usuario en una dirección aleatoria dentro del área definida por `width` y `height`. El método `info` devuelve información sobre el usuario.

- `Area`: Representa el área en la que se desarrolla la simulación. Tiene un ancho (`width`) y una altura (`height`). El método `addUsers` agrega los usuarios al área y los muestra en el gráfico. El método `addAccessPoints` agrega los puntos de acceso y los muestra en el gráfico. El método `drawArea` dibuja el área en el gráfico.

- `AccessPoint`: Representa un punto de acceso en la red. Cada punto de acceso tiene un identificador (`id`), una posición (`position`), una frecuencia (`frequency`), una potencia (`power`) y un ancho de banda (`bandwidth`). El método `info` devuelve información sobre el punto de acceso. El método `receivedPower` calcula la potencia de la señal recibida en un determinado rango de distancia. El método `SNR` calcula la relación señal-ruido en función de la distancia y la potencia de ruido. El método `bitRate` calcula la tasa de bits en función de la distancia y la potencia de ruido.

- `Simulator`: Es la clase principal que coordina la simulación. Recibe el ancho (`width`) y la altura (`height`) del área, el número de puntos de acceso (`AP`), la configuración de los puntos de acceso (`AP_config`), la lista de usuarios (`users`) y la potencia de ruido (`noise_power`). En el método `__init__`, se crean los puntos de acceso y se agregan los usuarios y los puntos de acceso al área. Luego, se calcula y muestra la tasa de bits de cada usuario con respecto a los puntos de acceso. El método `accessPoint` muestra información sobre los puntos de acceso. El método `update` se encarga de actualizar la posición de los usuarios en cada cuadro de la animación. El método `startSimulator` muestra el gráfico del área y la animación de movimiento de los usuarios.



1. receivedPower(distance)

### Simulator

1. width, determina el largo del área, su unidad es [m]
2. height, determina el ancho del área, su unidad es [m]
3. AP, determina la cantidad de access point dentro del simulador
