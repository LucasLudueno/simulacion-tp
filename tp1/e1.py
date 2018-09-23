from statistics import median
import matplotlib.pyplot as plt
from gcl import GCL

generator = GCL(a = 1013904223, c = 1664525, m = 2**32)

# Definimos la semilla como el promedio entre los padrones
seed = int(median([93081, 95475]))

# Ejecutamos el Generador Congruencial Lineal para N = 6 
times_to_execute = 6
result_list = generator.execute(seed, times_to_execute)
print(result_list)

# Ejecutamos el Generador Congruencial Lineal para N = 100.000
result_list_0_1 = generator.execute(seed, times = 100000, normalized = True)

# Graficamos el histograma de los resultados generados
plt.ylabel('Cantidad de resultados')
plt.xlabel('Probabilidad')
plt.hist(result_list_0_1, bins = 1000)
plt.show()
