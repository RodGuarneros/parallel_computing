import numpy as np
import time

while True:
    try:
        dimension = int(input("Introduzca el número de elementos para el vector A y B: "))
        if dimension <= 0:
            raise ValueError
        break
    except ValueError:
        print("La dimensión de los vectores debe ser un número entero y positiva")

VectorA = []
VectorB = []

print("Introduzca los elementos del vector A:")
for i in range(dimension):
    while True:
        try:
            value = float(input(f"Elemento {i + 1}: "))
            break
        except ValueError:
            print("Introduzca un número real (positivo o negativo).")
    VectorA.append(value)

print("Introduzca los elementos del vector B:")
for i in range(dimension):
    while True:
        try:
            value = float(input(f"Elemento {i + 1}: "))
            break
        except ValueError:
            print("Introduzca un número real (positivo o negativo).")
    VectorB.append(value)

# Start measuring time
start_time = time.time()

# Calculate the dot product
dot_product = np.sum(np.array(VectorA) * np.array(VectorB))

# Stop measuring time
end_time = time.time()

print("Producto Punto Total =", dot_product)
print(f"Tiempo de ejecucion: {end_time - start_time:.15f} segundos")