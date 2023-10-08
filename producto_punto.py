# Código paralelizado para calcular el producto escalar de dos vectores
# Basado en python y ejecutado en MS-MPI
# La línea de comando en tu terminal o gitbash debe ser: $ mpiexec -np 4 python producto_punto.py
# Elaboró: Rodrigo Guarneros

# Dependencias
from mpi4py import MPI
import numpy as np
import time


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# para el rank 0
if rank == 0:
    while True:
        try:
            dimension = int(input("Introduce el numero de elementos que tendran los vectores A y B: "))
            if dimension <= 0:
                raise ValueError
            break
        except ValueError:
            print("Las dimensiones de los vectores son numeros enteros positivos")

    VectorA = []
    VectorB = []

    print("Introduce los lementos del vector A:")
    for i in range(dimension):
        while True:
            try:
                value = float(input(f"Elemento {i + 1}: "))
                break
            except ValueError:
                print("Por favor, introduce un numero real valido.")
        VectorA.append(value)

    print("Introduce los lementos del vector B:")
    for i in range(dimension):
        while True:
            try:
                value = float(input(f"Elemento {i + 1}: "))
                break
            except ValueError:
                print("Por favor, introduce un numero real valido.")
        VectorB.append(value)

    # Transmite la dimensión y cada vector (A y B) a los ranks
    comm.bcast(dimension, root=0)
    comm.bcast(VectorA, root=0)
    comm.bcast(VectorB, root=0)
else:
    dimension = comm.bcast(None, root=0)
    VectorA = comm.bcast(None, root=0)
    VectorB = comm.bcast(None, root=0)

# REvisar si tienen la misma dimensión los vectores para garantizar que se puede hacer el producto punto
if len(VectorA) != dimension or len(VectorB) != dimension:
    if rank == 0:
        print("Los vectores deben tener la misma dimensión, por favor introduce una dimensión valida.")
else:
    # Se distribuyen los elementos de los vectores para cada proceso
    local_dimension = dimension // size
    start = rank * local_dimension
    end = start + local_dimension

    local_VectorA = VectorA[start:end]
    local_VectorB = VectorB[start:end]
    # Se mide el tiempo inicial

    local_start_time = time.time()

    # Se calcula el producto punto (1 de 2 cálculos matemáticos en este algoritmo) :)
    producto_punto = np.sum(np.array(local_VectorA) * np.array(local_VectorB))

    # Se obtiene el producto punto total o global (2 de 2 cálculos mateméticos en este algoritmo)
    global_dot_product = comm.reduce(producto_punto, op=MPI.SUM, root=0)

    # Se registra tiempo de conclusión
    local_end_time = time.time()

    if rank == 0:
        print("Total =", global_dot_product)
        print(f"Tiempo de ejecucion: {local_end_time - local_start_time} segundos")