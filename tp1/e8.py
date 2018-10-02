import statistics
import random
import numpy
import scipy.stats as stats
import matplotlib.pyplot as plt

CANTIDAD_MUESTRAS = 100000
NIVEL_SIGNIFICACION = 0.01

# Cantidad de pasos para que de cara una moneda
def stepsForHead():
   count=0
   num = random.uniform(0,1)
   while(num<=0.5):
       count+=1
       num = random.uniform(0,1)
   return count   

# Paso 1. Calculamos la cantidad de caras que se necesitan para 10.000 intentos
stepsCount = list()
for x in range(0, CANTIDAD_MUESTRAS):
   stepsCount.append(stepsForHead())

# Paso 2. Calculamos la distribucion acumulada
steps = {}
for count in stepsCount:
    if count in steps:
        steps[count] += 1
    else:
        steps[count] = 1

stepList = []
for key in steps:
    stepList.append(steps[key])

sortedList = sorted(stepList, reverse=True)
sumatory = sum(sortedList)
normalized_distr = [x/sumatory for x in sortedList]

# Paso 3: Ejecutamos el Test de Chi 2 para los valores obtenidos
D, pval = stats.chisquare(normalized_distr)

# Paso 4: Analizamos si se cumple nuestra hipotesis
if pval < NIVEL_SIGNIFICACION:
 print('Rechazamos la hipotesis')
else:
 print('Aceptamos la hipotesis')
