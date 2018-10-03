import statistics 
import random
import matplotlib.pyplot as plt

CANTIDAD_MUESTRAS = 100000

# Devuelve la cantidad de pasos para que de cara una moneda
def stepsForHead():
    count=0
    num = random.uniform(0,1)
    while(num<=0.5):
        count+=1
        num = random.uniform(0,1)
    return count    

# Calculamos la cantidad de caras que se necesitan para 100.000 intentos
stepsCount = list()
for x in range(0, CANTIDAD_MUESTRAS):
    stepsCount.append(stepsForHead())

print ("la media es: ", statistics.mean(stepsCount))
print ("la mediana es: ", statistics.median(stepsCount))
print ("la varianza es: ", statistics.variance(stepsCount))
print ("la moda es: ", statistics.mode(stepsCount))

plt.ylabel('Cantidad de aciertos')
plt.xlabel('Intentos')
plt.hist(stepsCount, bins = 1000)
plt.show()
