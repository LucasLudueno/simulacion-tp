import statistics
import matplotlib.pyplot as plt
from statistics import median
from gcl import GCL
from mpl_toolkits.mplot3d import axes3d, Axes3D

CANTIDAD_MUESTRAS = 100000

generator = GCL(a = 1013904223, c = 1664525, m = 2**32)
seed = int(median([93081, 95475]))

# Ejecutamos el Generador Congruencial Lineal para N = 100.000
result_list_0_1 = generator.execute(seed, times = CANTIDAD_MUESTRAS, normalized = True)

# Armamos el Test espectral de 2 y 3 dimensiones
xax = []
ya = []
zeta = []

for x in range(0, len(result_list_0_1) - 1,3):
    xax.append(result_list_0_1[x])
    
for y in range(1, len(result_list_0_1) - 2,3):
    ya.append(result_list_0_1[y])

for z in range(2, len(result_list_0_1) - 1,3):
    zeta.append(result_list_0_1[z])

fig = plt.figure(figsize=(20,20))

ax = Axes3D(fig)
ax.scatter(xax, ya, zeta, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
