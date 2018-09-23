import math
import matplotlib.pyplot as plt
from statistics import median, variance, mode, StatisticsError
from gcl import GCL

generator = GCL(a = 1013904223, c = 1664525, m = 2**32)
seed = int(median([93081, 95475]))

# Ejecutamos el Generador Congruencial Lineal para N = 100.000
result_list_0_1 = generator.execute(seed, times = 100000, normalized = True)

# Aplicamos la transformacion inversa para la exponencial negativa de media 15
lamb = 1/float(15)
inverted_list = [-1 * math.log(1 - x) / lamb for x in result_list_0_1]

# Calculamos la mediana, la varianza y la moda
media = median(inverted_list)
varianza = variance(inverted_list)

try:
    moda = mode(inverted_list)
except StatisticsError as e:
    moda = 0
 
print("la mediana es: ", media)
print("la varianza es: ",  varianza)
print("la moda es: ", moda)

# Graficamos el histograma de los resultados generados
plt.ylabel('Cantidad de resultados')
plt.xlabel('Probabilidad')
plt.hist(inverted_list, bins = 1000)
plt.show()
