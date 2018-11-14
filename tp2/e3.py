import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import statistics

CANTIDAD_ITERACIONES = 100
ESTADOS_INICIALES = [-1, 0, 1]

def x_func(x, y):
    return float(x)/2 + float(y)

def y_func(x, y):
    return float(y) - float(x)/2

def z_func(x, y, z):
    return float(z) - (float(x) + float(y))

def simulation(ax_to_variate):
    for i in ESTADOS_INICIALES:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for j in ESTADOS_INICIALES:
            for k in ESTADOS_INICIALES:
                if ax_to_variate == 'x':
                    current_x = i
                    current_y = j
                    current_z = k
                elif ax_to_variate == 'y':
                    current_y = i
                    current_x = j
                    current_z = k
                elif ax_to_variate == 'z':
                    current_z = i
                    current_x = j
                    current_y = k

                x_axis = [current_x]
                y_axis = [current_y]
                z_axis = [current_z]

                for c in range(1, CANTIDAD_ITERACIONES):
                    current_x = x_func(current_x, current_y)
                    current_y = y_func(current_x, current_y)
                    current_z = z_func(current_x, current_y, current_z)

                    x_axis.append(current_x)
                    y_axis.append(current_y)
                    z_axis.append(current_z)

                # Graficamos en 2D los resultados para X e Y (descomentar las lineas siguientes y comentar la graficacion 3D)
                # plt.xlabel('Estado X. Inicial =' + str(i))
                # plt.ylabel('Estado Y. Inicial =' + str(j))
                # plt.plot(x_axis, y_axis)
                # plt.show()

                # Graficamos en 3D los resultados
                ax.set_xlabel('Estado X')
                ax.set_ylabel('Estado Y')
                ax.set_zlabel('Estado Z')

                if ax_to_variate == 'x':
                    ax.set_xlabel('Estado X. Inicial =' + str(i))
                elif ax_to_variate == 'y':
                    ax.set_ylabel('Estado Y. Inicial =' + str(i))
                elif ax_to_variate == 'z':
                    ax.set_zlabel('Estado Z. Inicial =' + str(i))

                for l in range(1, CANTIDAD_ITERACIONES):
                    ax.scatter(x_axis[l], y_axis[l], z_axis[l])
        plt.show()

simulation(ax_to_variate = 'x')
simulation(ax_to_variate = 'y')
simulation(ax_to_variate = 'z')
