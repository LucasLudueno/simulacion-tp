import math
from statistics import median
from gcl import GCL
from skidmarks import gap_test

CANTIDAD_MUESTRAS = 100000
NIVEL_SIGNIFICACION = 0.05

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


start = 0.5
end = 1
gap_concatenation = ''
for number in result_list_0_1:
  if number >= start and number <= end:
    gap_concatenation += '1'
  elif number < start:
    gap_concatenation += '0'
  else:
    gap_concatenation += '2'

print(gap_concatenation)
result = gap_test(gap_concatenation, item = '1')

print(result['p'])
if result['p'] < NIVEL_SIGNIFICACION:
  print('Rechazamos la hipotesis')
else:
  print('Aceptamos la hipotesis')
