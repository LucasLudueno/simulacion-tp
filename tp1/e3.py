import statistics 
import seaborn as sns
import math
import numpy
import matplotlib.pyplot as plt
from statistics import median, variance, mode, StatisticsError
from gcl import GCL

CANTIDAD_MUESTRAS = 100000

# Coordenadas de una distribucion normal acumulada
X_COORD_POINTS = [0,  0.00003, 0.00135, 0.00621, 0.02275, 0.06681, 0.11507, 0.15866, 0.21186, 0.27425, 0.34458, 0.42074, 0.5, 0.57926, 0.65542, 0.72575, 0.78814, 0.84134, 0.88493, 0.93319, 0.97725, 0.99379, 0.99865, 0.99997]
Y_COORD_POINTS = [-5, -4,      -3 ,     -2.5 ,   -2,      -1.5 ,   -1.2 ,   -1 ,     -0.8 ,   -0.6,    -0.4 ,   -0.2 ,   0 ,  0.2 ,    0.4,     0.6 ,    0.8,     1,       1.2,     1.5,     2,       2.5,     3,       4.5]

# Ejecutamos el Generador Congruencial Lineal para N = 100.000
generator = GCL(a = 1013904223, c = 1664525, m = 2**32)
seed = int(median([93081, 95475]))
generated_points = generator.execute(seed, times = CANTIDAD_MUESTRAS, normalized = True)

# Calculamos la interpolacion de los puntos que generamos segun la transformacion inversa
result_list = numpy.interp(generated_points, X_COORD_POINTS, Y_COORD_POINTS)

# Calculamos la mediana, la varianza y la moda
media = median(result_list)
varianza = variance(result_list)

try:
    moda = mode(result_list)
except StatisticsError as e:
    moda = 0
 
print("la mediana es: ", media)
print("la varianza es: ",  varianza)
print("la moda es: ", moda)

# Graficamos el histograma de la distribucion normal generada
plt.hist(result_list, bins = 1000)
plt.show()
