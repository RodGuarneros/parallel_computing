# Código paralelizado para calcular el producto escalar de dos vectores
# Basado en python y ejecutado en MS-MPI
# La línea de comando en tu terminal o gitbash debe ser: $ mpiexec -np 4 python producto_punto.py
# Elaboró: Rodrigo Guarneros

from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    try:
        dimension = int(input("Introduzca el número de elementos para el vector A y B: "))
        if dimension <= 0:
            raise ValueError
    except ValueError:
        print("Las dimensiones de los vectores deben ser números enteros positivos.")
        exit(1)

    VectorA = np.zeros(dimension)
    VectorB = np.zeros(dimension)

    print("Introduzca los elementos del vector A:")
    for i in range(dimension):
        while True:
            try:
                VectorA[i] = float(input(f"Elemento {i + 1}: "))
                break
            except ValueError:
                print("Por favor, introduzca un número real válido para el vector A.")

    print("Introduzca los elementos del vector B:")
    for i in range(dimension):
        while True:
            try:
                VectorB[i] = float(input(f"Elemento {i + 1}: "))
                break
            except ValueError:
                print("Por favor, introduzca un número real válido para el vector B.")

else:
    dimension = None
    VectorA = None
    VectorB = None

dimension = comm.bcast(dimension, root=0)
VectorA = comm.bcast(VectorA, root=0)
VectorB = comm.bcast(VectorB, root=0)

if len(VectorA) != dimension or len(VectorB) != dimension:
    if rank == 0:
        print("Los vectores deben tener la misma dimensión, por favor introduce una dimensión válida.")
else:
    local_dimension = dimension // size
    start = rank * local_dimension
    end = start + local_dimension

    local_VectorA = VectorA[start:end]
    local_VectorB = VectorB[start:end]

    local_dot_product = np.dot(local_VectorA, local_VectorB)

    global_dot_products = comm.gather(local_dot_product, root=0)

    if rank == 0:
        dot_product_total = sum(global_dot_products)
        start_time = time.time()
        end_time = time.time()

        print(f"Producto Punto Total = {dot_product_total}")
        print(f"Tiempo de ejecucion: {end_time - start_time:.15f} segundos")
