import math
import random
import numpy
import scipy.stats as stats
import matplotlib.pyplot as plt
from statistics import median, variance, mode, StatisticsError
from gcl import GCL

CANTIDAD_MUESTRAS = 100000
NIVEL_SIGNIFICACION = 0.01

def p(x):
  c = math.sqrt(2 * math.exp(1) / math.pi)
  return normal(x) / (c * exp(x))

def exp(x): # exponencial negativa media 1
  return math.exp(x * -1)

def normal(x): # normal estandar
  return math.exp(-1 * (x**2) / 2) / math.sqrt(2 * math.pi)

def calculate_intervals(media, cant):
  interval_list = []
  lenght = int(cant / 2)

  for i in reversed(range(lenght - 1)): # puntos negativos
    begin = media/lenght * (i + 1) * -1
    end = media/lenght * i * -1
    interval_list.append((begin, end))

  for i in range(0, lenght): # puntos positivos
    begin = media/lenght * i
    end = media/lenght * (i + 1)
    interval_list.append((begin, end))
  
  return interval_list

def empiric_fuc(distr_list, intervals):
  empiric_distr = []

  for i in range(len(intervals)):
    empiric_distr.append(0)
    interval = intervals[i]

    for x in distr_list:
      if interval[0] <= x and x < interval[1]:
        empiric_distr[i] += 1
    
    if i != 0:
      empiric_distr[i] += empiric_distr[i - 1]
  
  return empiric_distr
    

# Paso 1: Generamos 100000 muestras de una variable exponencial
exponential_samples = [numpy.random.exponential(1) for x in range(CANTIDAD_MUESTRAS)]

# Paso 2: Aplicamos cada una de las muestras a nuestra funcion de probabilidad y en base a ello las elegimos
normal_list = []

for i in range(CANTIDAD_MUESTRAS):
  sample = exponential_samples[i]
  r = random.random()

  if r < p(sample):
    r2 = random.random()

    if (r2 < 0.5): # con prob 0.5 lo dejo positivo
      normal_list.append(sample)
    else:
      normal_list.append(sample * -1)


# Paso 3: Teniendo los valores de la normal, ejecutamos el Test de Kolmogorov
# para una normal estandar (no hace falta aplicar la transformacion lineal)
D, pval = stats.kstest(normal_list, 'norm')

if pval < NIVEL_SIGNIFICACION:
  print('Rechazamos la hipotesis')
else:
  print('Aceptamos la hipotesis')

# Calculo la funcion empirica de la distribucion generada
intervals = calculate_intervals(3, 10) #calculo para 10 intervalos y media 3
points_x = [x[1] for x in intervals]
empiric_points_y = empiric_fuc(normal_list, intervals)

# Calculo la funcion de acumulacion para la funcion real
normal_point = numpy.random.normal(0, 1, len(normal_list))
empiric_real_points_y = empiric_fuc(normal_point, intervals)

# Normalizamos ambos vectores
max_value_to_normalize_generated = max(empiric_points_y)
max_value_to_normalize_real = max(empiric_real_points_y)

# Graficamos
plt.plot(points_x, [x / max_value_to_normalize_generated for x in empiric_points_y ], label='Distr acumulacion generada')
plt.plot(points_x, [x / max_value_to_normalize_generated for x in empiric_real_points_y ], label='Distr acumulacion real')
plt.legend()
plt.show()
