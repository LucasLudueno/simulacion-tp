import random
import numpy as np
import matplotlib.pyplot as plt
import statistics

CANTIDAD_MUESTRAS = 100000

centralized = []
distributed = []
no_processed_centralized = 0
no_processed_distributed = 0

# Simulamos las solicitudes para la opcion 1 (DB centralizada)
for x in range(0, CANTIDAD_MUESTRAS):
    time_to_arrive = np.random.poisson(4)
    time_to_process = np.random.poisson(0.8)
    if time_to_process == 0:
        no_processed_centralized += 1
    centralized.append(time_to_arrive + time_to_process)
    
# Simulamos las solicitudes para la opcion 2 (DB distribuida)
for x in range(0, CANTIDAD_MUESTRAS):
    time_to_arrive = np.random.poisson(4)
    rand = random.random()

    if rand < 0.6:
        time_to_process = np.random.poisson(0.7)
    else:
        time_to_process = np.random.poisson(1)
    if time_to_process == 0:
        no_processed_distributed += 1
    distributed.append(time_to_arrive + time_to_process)

# Calculamos el tiempo medio para las opciones
print("Tiempo medio para opcion DB distribuida: ", statistics.mean(distributed))
print("Tiempo medio para opcion DB centralizada: ", statistics.mean(centralized))

# Calculamos la fraccion que no tuvo que esperar para ser procesada
print("Fraccion de solicitudes que no esperaron a ser procesada para opcion DB distribuida: ", float(no_processed_distributed) / CANTIDAD_MUESTRAS)
print("Fraccion de solicitudes que no esperaron a ser procesada para opcion DB centralizada: ", float(no_processed_centralized) / CANTIDAD_MUESTRAS)
