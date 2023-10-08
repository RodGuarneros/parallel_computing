import sys
from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 10  # Tamaño de la matriz
if len(sys.argv) > 1:
    n = int(sys.argv[1])

# Asegurar que la matriz sea consistente en dimensiones con el número de procesos (np)
if n % size != 0:
    if rank == 0:
        print("El tamaño de la matriz (n) debe ser divisible por el número de procesos (np).")
    sys.exit(1)

local_n = n // size

local_A = np.zeros((local_n, n), dtype=int)
local_x = np.zeros(n, dtype=int)
local_result = np.zeros(local_n, dtype=int)
result = None

# Inicializando la matriz y el vector
A = None
x = None

if rank == 0:
    A = np.random.randint(1, 1000, size=(n, n), dtype=int)
    x = np.random.randint(1, 100, size=n, dtype=int)

# Transmitir la matriz a todos los procesos
A = comm.bcast(A, root=0)

# Transmitir el vector x a todos los procesos
comm.Scatter(x, local_x, root=0)

# Las matemáticas del producto punto
for i in range(local_n):
    for j in range(n):
        local_result[i] += A[i + rank * local_n][j] * local_x[j]

# Obtener los resultados locales para hacer el resultado global
if rank == 0:
    result = np.zeros(n, dtype=int)

comm.Gather(local_result, result, root=0)

if rank == 0:
    print("Matriz A:")
    print(A)
    print("Vector x:")
    print(x)
    print("Resultado:")
    print(result)

start_time = time.time()

end_time = time.time()

if rank == 0:
    print("Tiempo de ejecución: {:.10f} segundos".format(end_time - start_time))
