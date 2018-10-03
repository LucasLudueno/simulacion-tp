import math
from statistics import mean
from gcl import GCL
import scipy.stats as stats

CANTIDAD_MUESTRAS = 100000
NIVEL_SIGNIFICACION = 0.01

def gaps_out_inteval(start, end, numbers_list):
 gaps_list = []
 gaps_count = 0

 is_out_interval = False
 for number in numbers_list:
    if number < start or number > end:
      gaps_count += 1
      is_out_interval = True
    else:
      if is_out_interval:
        gaps_list.append(gaps_count)
      gaps_count = 0
      is_out_interval = False

 if is_out_interval:
   gaps_list.append(gaps_count)

 return gaps_list

def execute_gap_test(random_list, interval_start, interval_end, signification_level):
 # Utilizamos el metodo de GAP Test
 # Paso 1: Calculamos el vector de gaps que no ocurrieron en cada intervalo
 gaps_intervals = gaps_out_inteval(interval_start, interval_end, random_list)

 print(random_list)
 print(gaps_intervals)

 # Paso 2: Calculamos el numero de intervalos esperados segun su tamaño
 max_interval = max(gaps_intervals)
 expected_count_for_interval = []

 P = interval_end - interval_start
 for i in range(1, max_interval):
   expected = P * ((1 - P)**(i - 1)) * CANTIDAD_MUESTRAS
   expected_count_for_interval.append(expected)

 # Paso 3: Normalizamos el vector de cantidad de intervalos segun su tamaño
 sumatory = sum(expected_count_for_interval)
 normalized_interval = [x / sumatory for x in expected_count_for_interval]

 # Paso 4: Aplicamos el test de chi2 para la distribucion
 D, pval = stats.chisquare(normalized_interval)
 if pval < NIVEL_SIGNIFICACION:
   print('Rechazamos la hipotesis en el intervalo:', interval_start, interval_end)
 else:
   print('Aceptamos la hipotesis en el intervalo:', interval_start, interval_end)


# Ejecutamos el Generador Congruencial Lineal para N = 100.000
generator = GCL(a = 1013904223, c = 1664525, m = 2**32)
seed = int(mean([93081, 95475]))
result_list_0_1 = generator.execute(seed, times = CANTIDAD_MUESTRAS, normalized = True)

# Utilizamos el metodo de GAP Test para los dos intervalos
execute_gap_test(result_list_0_1, 0.2, 0.6, NIVEL_SIGNIFICACION)
execute_gap_test(result_list_0_1, 0.5, 1, NIVEL_SIGNIFICACION)
