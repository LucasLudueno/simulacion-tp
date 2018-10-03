import math
import random
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from statistics import mean, variance, mode, StatisticsError
from gcl import GCL

MEDIA = 35
DESVIO = 5
CANTIDAD_MUESTRAS = 100000

def p(x):
  c = math.sqrt(2 * math.exp(1) / math.pi)
  return normal(x) / (c * exp(x))

def exp(x, media = 1): # exponencial negativa media 1
  return math.exp(x * -1)

def normal(x): # normal estandar
  return math.exp(-1 * (x**2) / 2) / math.sqrt(2 * math.pi)


# Paso 1: Generamos 100000 muestras de una variable exponencial
exponential_samples = [numpy.random.exponential(1) for x in range(CANTIDAD_MUESTRAS)]

# Paso 2: Aplicamos cada una de las muestras a nuestra funcion de probabilidad y en base a ello las elegimos
result_list = []

for i in range(CANTIDAD_MUESTRAS):
  sample = exponential_samples[i]
  r = random.random()

  if r < p(sample):
    r2 = random.random()

    if (r2 < 0.5): # con prob 0.5 lo dejo positivo
      result_list.append(sample)
    else:
      result_list.append(sample * -1)

# Aplicamos la transformacion lineal para media = 35, desvio = 5
transformation_list = [x * DESVIO + MEDIA for x in result_list]

# Calculamos la media, la varianza y la moda
media = mean(transformation_list)
varianza = variance(transformation_list)

try:
   moda = mode(transformation_list)
except StatisticsError as e:
   moda = 0

print("la media es: ", media)
print("la varianza es: ",  varianza)
print("la moda es: ", moda)

# Graficamos el histograma de los resultados generados y los comparamos con la normal real de media 35 y desvio 5
real_normal = numpy.random.normal(MEDIA, DESVIO, 35000)

plt.hist(transformation_list, align='mid', bins = 1000, label = 'Normal generada')
plt.hist(real_normal, histtype='step', align='mid', bins = 1000, label = 'Normal real')
plt.legend()
plt.show()
