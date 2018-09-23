import math
import random
import numpy
import matplotlib.pyplot as plt
from statistics import median, variance, mode, StatisticsError
from gcl import GCL

CANTIDAD_MUESTRAS = 100000

def p(x):
  media = 1
  desvio = 1
  c = math.sqrt(2 * math.exp(media) / math.pi)
  return normal(x, media, desvio) / (c * exp(x, media))

def exp(x, media = 1):
  return math.exp(x * media)

def normal(x, media = 1, desvio = 1):
  return math.exp(- (x - media)**2 / 2*(desvio**2) ) / ( math.sqrt(2 * math.pi) * desvio )


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

# Graficamos el histograma de los resultados generados
plt.hist(result_list, bins = 1000)
plt.show()
