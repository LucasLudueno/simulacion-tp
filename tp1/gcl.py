class GCL:
  # a: multiplicador
  # c: incremento
  # m: modulo
  def __init__(self, a, c, m):
    self.a = a
    self.c = c
    self.m = m

  # times: cantidad de ejecuciones
  def execute(self, X, times, normalized = False):
    result_list = list()

    for i in range(0, times):
      X_plus_one = (self.a * X + self.c) % self.m
      result_list.append(X_plus_one)
      X = X_plus_one
    
    if (normalized):
      return [x / float(self.m) for x in result_list] # normalizamos en funcion del modulo utilizado
    return result_list
