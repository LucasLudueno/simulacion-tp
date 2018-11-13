import random
import numpy as np
import matplotlib.pyplot as plt
import statistics

CANTIDAD_MUESTRAS = 100000

centralized = []
distributed = []

# Simulamos las solicitudes para la opcion 1 (DB centralizada)
for x in range(0, CANTIDAD_MUESTRAS):
    time_to_arrive = np.random.poisson(4)
    time_to_process = np.random.poisson(0.8)
    centralized.append(time_to_arrive + time_to_process)
    
# Simulamos las solicitudes para la opcion 2 (DB distribuida)
for x in range(0, CANTIDAD_MUESTRAS):
    time_to_arrive = np.random.poisson(4)
    rand = random.random()

    if rand < 0.6:
        time_to_process = np.random.poisson(0.7)
    else:
        time_to_process = np.random.poisson(1)
    distributed.append(time_to_arrive + time_to_process)

# Calculamos el tiempo medio para las opciones
print("Tiempo medio para opcion DB distribuida: ", statistics.mean(distributed))
print("Tiempo medio para opcion DB centralizada: ", statistics.mean(centralized))
