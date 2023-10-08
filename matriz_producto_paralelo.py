# Código paralelizado para calcular producto punto matriz y vector x
# Basado en python y ejecutado en MS-MPI
# La línea de comando en tu terminal o gitbash debe ser: $ mpiexec -np 4 python matriz_producto_paralelo.py
# Elaboró: Rodrigo Guarneros


import sys
from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 10  # Default size of the matrix

if rank == 0:
    n = int(input("Introduce el tamaño de la matriz (n): "))  # Input for matrix dimension

# Broadcast the matrix dimension to all processes
n = comm.bcast(n, root=0)

# Ensure that the matrix dimension is consistent with the number of processes (size)
if n % size != 0:
    if rank == 0:
        print("El tamano de la matriz (n) debe ser divisible por el numero de procesos (np).")
    sys.exit(1)

local_n = n // size

local_A = np.zeros((local_n, n), dtype=int)
local_x = np.zeros(n, dtype=int)
local_result = np.zeros(local_n, dtype=int)
result = None

# Initialize the matrix and vector
A = None
x = None

if rank == 0:
    A = np.random.randint(1, 1000, size=(n, n), dtype=int)
    x = np.random.randint(1, 100, size=n, dtype=int)

# Transmit the matrix to all processes
A = comm.bcast(A, root=0)

# Transmit the vector x to all processes
comm.Scatter(x, local_x, root=0)

# Perform matrix-vector multiplication
for i in range(local_n):
    for j in range(n):
        local_result[i] += A[i + rank * local_n][j] * local_x[j]

# Gather the local results to compute the global result
if rank == 0:
    result = np.zeros(n, dtype=int)

comm.Gather(local_result, result, root=0)

if rank == 0:
    print("Matriz A:")
    print(A)
    print("Vector x:")
    print(x)
    print("Resultado del producto punto del vector x y matriz:")
    print(result)

start_time = time.time()
end_time = time.time()

if rank == 0:
    print("Tiempo de ejecucion: {:.10f} segundos".format(end_time - start_time))