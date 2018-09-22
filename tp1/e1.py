from statistics import median
import seaborn as sns

def gcl(X, times, normalized = False):
  result_list = list()
  a = 1013904223 # multiplicador
  c = 1664525    # incremento
  m = 2**32      # modulo

  for i in range(0, times):
    X_plus_one = (a * X + c) % m
    result_list.append(X_plus_one)
    X = X_plus_one
  
  if (normalized):
    return [x / float(m) for x in result_list] # normalizamos en funcion del modulo utilizado
  return result_list


seed = int(median([93081, 95475]))

# Ejecutamos el Generador Congruencial Lineal para N = 6 
times_to_execute = 6
result_list = gcl(seed, times_to_execute)
print(result_list)

# Ejecutamos el Generador Congruencial Lineal para N = 100.000
times_to_execute = 100000
result_list_0_1 = gcl(seed, times_to_execute, normalized = True)

# Graficamos el histograma de los resultados generados
print(result_list_0_1)
sns.set_style('darkgrid')
sns.distplot(result_list_0_1)
