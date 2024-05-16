import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir los vértices del cubo
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])

# Definir las aristas del cubo
aristas = [[0, 1], [1, 2], [2, 3], [3, 0],
           [4, 5], [5, 6], [6, 7], [7, 4],
           [0, 4], [1, 5], [2, 6], [3, 7]]

# Crear la visualización del cubo
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar las aristas del cubo
for arista in aristas:
    ax.plot3D(*zip(vertices[arista[0]], vertices[arista[1]]), color="green")

# Configurar los límites de los ejes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# Mostrar el gráfico
plt.show()