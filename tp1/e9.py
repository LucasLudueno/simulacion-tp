import math
from statistics import median
from gcl import GCL

CANTIDAD_MUESTRAS = 100000

def gaps_in_inteval(start, end, numbers_list):
  gaps_count = 0

  current_interval = False
  for number in result_list_0_1:
    if number >= start and number <= end:
      if not current_interval:
        gaps_count += 1

      current_interval = True
    else:
      current_interval = False
  
  return gaps_count

# Ejecutamos el Generador Congruencial Lineal para N = 100.000
generator = GCL(a = 1013904223, c = 1664525, m = 2**32)
seed = int(median([93081, 95475]))
result_list_0_1 = generator.execute(seed, times = CANTIDAD_MUESTRAS, normalized = True)

# Utilizamos el metodo de GAP Test
# Paso 1. Calculamos D teorica con nivel de significacion del 5%, para luego compararla
D = 1.36 / math.sqrt(CANTIDAD_MUESTRAS)

# Paso 2. Calculamos la cantidad de gaps que tiene cada intervalo
gaps_intervals_1 = gaps_in_inteval(0.2, 0.6, result_list_0_1)
gaps_intervals_2 = gaps_in_inteval(0.5, 1, result_list_0_1)

print(gaps_intervals_1)

# Paso 3. Encontramos D en base a los resultados obtenidos
frecuency_1 = gaps_intervals_1 / CANTIDAD_MUESTRAS
frecuency_2 = gaps_intervals_2 / CANTIDAD_MUESTRAS

F1 = 1 - 0.6 ** (4 + 1) # Distribucion de frecuencias teorica aplicada al intervalo 0.2 - 0.6
F2 = 1 - 0.6 ** (5 + 1) # Distribucion de frecuencias teorica aplicada al intervalo 0.5 - 1

# Paso 4. Comparamos D actual con D calculado teoricamente
D1 = F1 - frecuency_1
D2 = F2 - frecuency_2

if (D1 > D):
  print('Rechazamos la hipotesis 1')
else:
  print('Aceptamos la hipotesis 1')

if (D2 > D):
  print('Rechazamos la hipotesis 2')
else:
  print('Aceptamos la hipotesis 2')
