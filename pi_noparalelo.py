import math
import time

n = 0
precision = 0
PI25DT = 3.141592653589793238462643
h, local_sum, pi = 0.0, 0.0, 0.0

# El número de divisiones del intervalo y el factor de precisión (decimales)
n = int(input("Introduzca el valor de n para la suma de Rimann: "))
precision = int(input("Instroduzca el valor de precision: "))

# Registro del tiempo de inicio parte paralela
start_time = time.time()

h = 1.0 / float(n)  # El tamaño de cada intervalo
local_sum = 0.0  # Inicializa la suma

# Calculando la suma local con la fórmula proporcionada
for i in range(1, n + 1):
    x = h * (float(i) - 0.5)
    local_sum += (4.0 / (1.0 + x * x))

# Calculando pi
pi = local_sum * h

# Registro del tiempo final
end_time = time.time()

print("El valor aproximado de PI es: {:.15f}, con un error de {:.15f}".format(pi, abs(pi - PI25DT)))
print("Tiempo total de ejecucion: {:.20f} segundos".format(end_time - start_time))