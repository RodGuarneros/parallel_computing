# Código paralelizado para calcular PI a través de la suma de Riemann
# Basado en python y ejecutado en MS-MPI
# La línea de comando en tu terminal o gitbash debe ser: $ mpiexec -np 4 python pi_paralelo.py
# Elaboró: Rodrigo Guarneros

from mpi4py import MPI
import math
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 0
precision = 0
PI25DT = 3.141592653589793238462643
h, local_sum, global_sum, pi = 0.0, 0.0, 0.0, 0.0

if rank == 0:
    # Como insumos el numero de divisiones del intervalo y el factor de precisión
    # Entendido como el número de decimales que deseamos utilizar
    n = int(input("Indica el valor de n para la suma de Riemann: "))
    precision = int(input("Indica por favor el factor de precisión: "))

# Transmisión de 'n' y la 'precisión' del  process 0 a todos los procesos
n = comm.bcast(n, root=0)
precision = comm.bcast(precision, root=0)

# Inicia el proceso y se registra el tiempo inicial
start_time = MPI.Wtime()

h = 1.0 / float(n) # el tamaño de cada incremento dado n
local_sum = 0.0 # se inicializa la suma

# Calcula la suma local con la función proporcionada
for i in range(rank + 1, n + 1, size):
    x = h * (float(i) - 0.5)
    local_sum += (4.0 / (1.0 + x * x))

# Utiliza MPI para combinar las sumas locales dentro de la suma global
global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

# Se registr el tiempo de finalización del algorimo en su parte paralela
end_time = MPI.Wtime()

# Resultados: Se imprime el Rank (número de orden), size (cantidad de procesos mpi)
# y la suma local de cada proceso
print("Proceso {} de {} el Rank (número de orden) es: {}, Size (cantidad de procesos) es: {}, Suma local es: {}".format(rank, size, rank, size, local_sum))

# Se calcula PI
if rank == 0:
    pi = global_sum * h
    print("La aproximación del valor de PI es: {:.15f}, con un error de {:.15f}".format(pi, abs(pi - PI25DT)))
    print("Tiempo total de ejecución en la parte paralela: {:.10f} segundos".format(end_time - start_time))
