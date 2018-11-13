import random
import numpy as np
import matplotlib.pyplot as plt
import statistics

CANTIDAD_MUESTRAS = 100000

centralized = []
distributed = []
wating_time_centralized = 0
wating_time_distributed = 0
no_processed_centralized = 0
no_processed_distributed = 0
total_wating_time_centralized = 0
total_wating_time_distributed = 0

# Simulamos las solicitudes para la opcion 1 (DB centralizada)
current_time = 0

for x in range(0, CANTIDAD_MUESTRAS):
    time_to_arrive = np.random.poisson(4)
    time_to_process = np.random.poisson(0.8)

    if time_to_arrive > current_time:
        # la solicitud no tuvo que esperar nada
        no_processed_centralized += 1
        current_time = time_to_arrive + time_to_process
    else:
        wating_time = current_time - time_to_arrive
        wating_time_centralized = wating_time_centralized + wating_time
        current_time = wating_time + time_to_process
    total_wating_time_centralized = total_wating_time_centralized + current_time

# Simulamos las solicitudes para la opcion 2 (DB distribuida)
current_time_1 = 0
current_time_2 = 0
for x in range(0, CANTIDAD_MUESTRAS):
    time_to_arrive = np.random.poisson(4)
    rand = random.random()

    if rand < 0.6:
        current_time_2 = max(0, current_time_2 - time_to_arrive)
        time_to_process = np.random.poisson(0.7)
        if time_to_arrive > current_time_1:
            # la solicitud no tuvo que esperar
            no_processed_distributed += 1
            current_time_1 = time_to_arrive + time_to_process
        else:
            wating_time = current_time_1 - time_to_arrive
            wating_time_distributed = wating_time_distributed + wating_time
            current_time_1 = wating_time + time_to_process
        total_wating_time_distributed = total_wating_time_distributed + current_time_1
       
    else:
        current_time_1 = max(0, current_time_1 - time_to_arrive)
        time_to_process = np.random.poisson(1)
        if time_to_arrive > current_time_2:
            # la solicitud no tuvo que esperar nada
            no_processed_distributed += 1
            current_time_2 = time_to_arrive + time_to_process
        else:
            wating_time = current_time_2 - time_to_arrive
            wating_time_distributed = wating_time_distributed + wating_time
            current_time_2 = wating_time + time_to_process
        total_wating_time_distributed = total_wating_time_distributed + current_time_2

# Calculamos el tiempo medio de espera para las opciones
print("Tiempo medio de espera para opcion DB distribuida: ", float(wating_time_distributed)  / CANTIDAD_MUESTRAS)
print("Tiempo medio de espera para opcion DB centralizada: ", float(wating_time_centralized) / CANTIDAD_MUESTRAS)

# Calculamos la fraccion que no tuvo que esperar para ser procesada
print("Fraccion de solicitudes que no esperaron a ser procesada para opcion DB distribuida: ", float(no_processed_distributed) / CANTIDAD_MUESTRAS)
print("Fraccion de solicitudes que no esperaron a ser procesada para opcion DB centralizada: ", float(no_processed_centralized) / CANTIDAD_MUESTRAS)

# Calculamos el tiempo medio total para las opciones
print("Tiempo medio total para opcion DB distribuida: ", float(total_wating_time_distributed)  / CANTIDAD_MUESTRAS)
print("Tiempo medio total para opcion DB centralizada: ", float(total_wating_time_centralized) / CANTIDAD_MUESTRAS)
