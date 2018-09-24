import matplotlib.pyplot as plt
from statistics import median
from gcl import GCL

CANTIDAD_MUESTRAS = 100000

# Funcion empirica enunciada
def empiric_function(x):
  if ( x <= 0.5):
    return 1
  if ( x >= 0.5 and x <= 0.7):
    return 2
  if ( x >= 0.7 and x <= 0.8):
    return 3
  if ( x >= 0.8):
    return 4

generator = GCL(a = 1013904223, c = 1664525, m = 2**32)
seed = int(median([93081, 95475]))

# Ejecutamos el Generador Congruencial Lineal para N = 100.000
result_list_0_1 = generator.execute(seed, times = CANTIDAD_MUESTRAS, normalized = True)

# Aplicamos la transformacion inversa para las muestras generadas, a la funcion F
inverted_list = [empiric_function(x) for x in result_list_0_1]
D = { i: inverted_list.count(i) for i in set(inverted_list)}

# Graficamos el grafico de barras de los resultados
plt.ylabel('Cantidad de resultados')
plt.xlabel('Valor generado')
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))
plt.show()
