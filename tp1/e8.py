import statistics 
import random
import scipy.stats as stats
import matplotlib.pyplot as plt

CANTIDAD_MUESTRAS = 1000
NIVEL_SIGNIFICACION = 0.01

# Cantidad de pasos para que de cara una moneda
def stepsForHead():
    count=0
    num = random.uniform(0,1)
    while(num<=0.5):
        count+=1
        num = random.uniform(0,1)
    return count    

# Paso 1. Calculamos la cantidad de caras que se necesitan para 100.000 intentos
stepsCount = list()
for x in range(0, CANTIDAD_MUESTRAS):
    stepsCount.append(stepsForHead())

# Paso 2: Ejecutamos el Test de Chi 2 para los valores obtenidos
D, pval = stats.chisquare(stepsCount)

# Paso 3: Analizamos si se cumple nuestra hipotesis
if pval < NIVEL_SIGNIFICACION:
  print('Rechazamos la hipotesis')
else:
  print('Aceptamos la hipotesis')

