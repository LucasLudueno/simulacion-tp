import random
import numpy as np
import matplotlib.pyplot as plt
import statistics

ESTADO_INICIAL = 0
ESTADO_FINAL = 30
CANTIDAD_MUESTRAS = 10000000

# las probabilidades son son las calculadas en el enunciado
PROB_MENOS = float(13.0/400)
PROB_IGUAL_SIN_PROCESAR = float(377.0/400)
PROB_IGUAL_PROCESANDO = float(1.0/1200)

# Simulamos los procesamientos de solicitudes
current_state = ESTADO_INICIAL
states_along_time = []
without_processing_count = 0

for x in range(0, CANTIDAD_MUESTRAS):
    states_along_time.append(current_state)
    rand = random.random()

    # Cambiamos de estado de acuerdo a la matriz planteada
    if current_state == ESTADO_INICIAL:
        if rand < float(1.0/40):
            current_state += 1
            without_processing_count += 1 # suma cuando no se procesa una instruccion

    elif current_state == ESTADO_FINAL:
        if rand < float(1.0/30):
            current_state -= 1
        else:
            without_processing_count += 1 # suma cuando no se procesa una instruccion

    else:
        if rand <= PROB_MENOS:
            current_state -= 1
        elif rand > PROB_MENOS and rand < PROB_IGUAL_SIN_PROCESAR + PROB_MENOS:
            without_processing_count += 1 # suma cuando no se procesa una instruccion
        elif rand > PROB_IGUAL_SIN_PROCESAR + PROB_IGUAL_PROCESANDO + PROB_MENOS:
            current_state += 1

# Mostramos el porcentaje de tiempo sin procesar una solicitud
print("Porcentaje de tiempo sin procesar una solicitud:", float(without_processing_count) / CANTIDAD_MUESTRAS)

# Graficamos los estados a traves del tiempo
plt.ylabel('Estado')
plt.xlabel('Tiempo en milisegundos')
plt.plot(states_along_time)
plt.show()

# # Graficamos el histograma de los estados
plt.ylabel('Cantidad')
plt.xlabel('Estado')
plt.hist(states_along_time, bins = 1000)
plt.show()
