import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import statistics

CANTIDAD_ITERACIONES = 100
ESTADOS_INICIALES_X = [-1, 0, 1]
ESTADOS_INICIALES_Y = [-1, 0, 1]
ESTADOS_INICIALES_Z = [-1, 0, 1]

def x_func(x, y):
    return float(x)/2 + float(y)

def y_func(x, y):
    return float(y) - float(x)/2

def z_func(x, y, z):
    return float(z) - (float(x) + float(y))

# Simulamos las ejecuciones para las combinaciones del estado X
for x in ESTADOS_INICIALES_X:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for y in ESTADOS_INICIALES_Y:
        for z in ESTADOS_INICIALES_Z:
            current_x = x
            current_y = y
            current_z = z
            x_axis = [current_x]
            y_axis = [current_y]
            z_axis = [current_z]

            for i in range(1, CANTIDAD_ITERACIONES):
                current_x = x_func(current_x, current_y)
                current_y = y_func(current_x, current_y)
                current_z = z_func(current_x, current_y, current_z)

                x_axis.append(current_x)
                y_axis.append(current_y)
                z_axis.append(current_z)

            # Graficamos en 2D los resultados
            # plt.xlabel('Estado X. Inicial =' + str(x))
            # plt.ylabel('Estado Y. Inicial =' + str(y))
            # plt.plot(x_axis, y_axis)
            # plt.show()

            # Graficamos en 3D los resultados (descomentar las lineas siguientes y comentar la graficacion 2D)
            ax.set_xlabel('Estado X. Inicial =' + str(x))
            ax.set_ylabel('Estado Y')
            ax.set_zlabel('Estado Z')
            for j in range(1, CANTIDAD_ITERACIONES):
                ax.scatter(x_axis[j], y_axis[j], z_axis[j])
    plt.show()


# Simulamos las ejecuciones para las combinaciones del estado Y
for y in ESTADOS_INICIALES_X:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for x in ESTADOS_INICIALES_Y:
        for z in ESTADOS_INICIALES_Z:
            current_x = x
            current_y = y
            current_z = z
            x_axis = [current_x]
            y_axis = [current_y]
            z_axis = [current_z]

            for i in range(1, CANTIDAD_ITERACIONES):
                current_x = x_func(current_x, current_y)
                current_y = y_func(current_x, current_y)
                current_z = z_func(current_x, current_y, current_z)

                x_axis.append(current_x)
                y_axis.append(current_y)
                z_axis.append(current_z)

            # Graficamos en 3D los resultados
            ax.set_xlabel('Estado X')
            ax.set_ylabel('Estado Y. Inicial =' + str(y))
            ax.set_zlabel('Estado Z')
            for j in range(1, CANTIDAD_ITERACIONES):
                ax.scatter(x_axis[j], y_axis[j], z_axis[j])
    plt.show()


# Simulamos las ejecuciones para las combinaciones del estado Z
for z in ESTADOS_INICIALES_X:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for x in ESTADOS_INICIALES_Y:
        for y in ESTADOS_INICIALES_Z:
            current_x = x
            current_y = y
            current_z = z
            x_axis = [current_x]
            y_axis = [current_y]
            z_axis = [current_z]

            for i in range(1, CANTIDAD_ITERACIONES):
                current_x = x_func(current_x, current_y)
                current_y = y_func(current_x, current_y)
                current_z = z_func(current_x, current_y, current_z)

                x_axis.append(current_x)
                y_axis.append(current_y)
                z_axis.append(current_z)

            # Graficamos en 3D los resultados
            ax.set_xlabel('Estado X')
            ax.set_ylabel('Estado Y')
            ax.set_zlabel('Estado Z. Inicial =' + str(z))
            for j in range(1, CANTIDAD_ITERACIONES):
                ax.scatter(x_axis[j], y_axis[j], z_axis[j])
    plt.show()
