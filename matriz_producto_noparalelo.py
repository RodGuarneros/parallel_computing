import sys
import numpy as np
import time

n = 10  # Tamaño de la matriz
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(input("Introduce el tamano de la matriz (n): "))  # Preguntar por la dimensión n si no se proporciona como argumento

local_n = n

local_A = np.zeros((local_n, n), dtype=int)
local_x = np.zeros(n, dtype=int)
local_result = np.zeros(n, dtype=int)  # Cambiar la dimensión de local_result a n para que sea un vector
result = None

# Inicializando la matriz y el vector
A = np.random.randint(1, 1000, size=(n, n), dtype=int)
x = np.random.randint(1, 100, size=n, dtype=int)

# Las matemáticas del producto punto
for i in range(local_n):
    for j in range(n):
        local_result[i] += A[i][j] * x[j]

if result is None:
    result = np.zeros(n, dtype=int)

result = local_result  # Cambiar result para que sea igual a local_result (un vector)

print("Matriz A:")
print(A)
print("Vector x:")
print(x)
print("Resultado:")
print(result)

start_time = time.time()
end_time = time.time()

print("Tiempo de ejecucion: {:.10f} segundos".format(end_time - start_time))


# import sys
# import numpy as np
# import time

# n = 10  # Tamaño de la matriz
# if len(sys.argv) > 1:
#     n = int(sys.argv[1])

# local_n = n

# local_A = np.zeros((local_n, n), dtype=int)
# local_x = np.zeros(n, dtype=int)
# local_result = np.zeros(local_n, dtype=int)
# result = None

# # Inicializando la matriz y el vector
# A = np.random.randint(1, 1000, size=(n, n), dtype=int)
# x = np.random.randint(1, 100, size=n, dtype=int)

# # Las matemáticas del producto punto
# for i in range(local_n):
#     for j in range(n):
#         local_result[i] += A[i][j] * x[j]

# if result is None:
#     result = np.zeros(n, dtype=int)

# result = np.sum(local_result, axis=0)

# print("Matriz A:")
# print(A)
# print("Vector x:")
# print(x)
# print("Resultado:")
# print(result)

# start_time = time.time()
# end_time = time.time()

# print("Tiempo de ejecución: {:.10f} segundos".format(end_time - start_time))