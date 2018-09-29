import statistics 
import random
import numpy
import scipy.stats as stats
import matplotlib.pyplot as plt

CANTIDAD_MUESTRAS = 10
NIVEL_SIGNIFICACION = 0.01

# Cantidad de pasos para que de cara una moneda
def stepsForHead():
    count = 0
    num = random.uniform(0,1)

    while(num <= 0.5):
        count += 1
        num = random.uniform(0,1)
    return count    

# Paso 1. Calculamos la cantidad de caras que se necesitan para 100.000 intentos
stepsCount = list()
for x in range(1, CANTIDAD_MUESTRAS):
    stepsCount.append(stepsForHead())

# Paso 2: Ejecutamos el Test de Chi 2 para los valores obtenidos (comparado con una bernoulli)
expected_distrib = numpy.random.binomial(1, 0.5, CANTIDAD_MUESTRAS) # Bernoulli 0.5
print(expected_distrib)
print(stepsCount)
D, pval = stats.chisquare(stepsCount, f_exp = expected_distrib)
print(pval)

# Paso 3: Analizamos si se cumple nuestra hipotesis
if pval < NIVEL_SIGNIFICACION:
  print('Rechazamos la hipotesis')
else:
  print('Aceptamos la hipotesis')
