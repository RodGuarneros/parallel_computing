from mpi4py import MPI
import time

# Nota: El programa se guarda en el archivo mensajes_paralelo2.py y se ejecuta con base en MS MPI
# La línea de comando es: $ mpiexec -n 4 python mensajes_paralelo2.py
# Elaboró: Rodrigo Guarneros Gutiérrez 

# dependencias
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# preguntar por el número de procesos, debe ser menor al número de núcleos especificados en mpiexec, por ejemplo 
#  mpiexec -n 4 python mensajes_paralelo2.py
if rank == 0:
    num_processes = int(input("Introudce por favor el número de procesos (entre 2 y el número de núcleos): "))
else:
    num_processes = None


# Se transmite el número de procesos seleccionado por el usuario
num_processes = comm.bcast(num_processes, root=0)

# Se registra el tiempo inicial
start_time = time.time()

received_message = "Este mensaje es para"
received_initial = "Hola soy el proceso 0"

if rank == 0:
    print(received_initial)


# Envío y recepción encadenada de los mensajes
for i in range(1, num_processes):
    if rank == i:
        received_message = comm.recv(source=i-1)
        print(f"Soy el proceso {rank} y he recibido el mensaje de {i - 1} que dice: {received_message}")
    elif rank == i - 1:
        message = received_initial
        comm.send(message, dest=i)

# Se registra el tiempo de finalización del algoritmo
end_time = time.time()

# Se calcula el tiempo total de ejecución
total_elapsed_time = comm.reduce(end_time - start_time, op=MPI.SUM, root=0)

# Se imprime el tiempo total para conocimiento del usuario
if rank == 0:
    print(f"El tiempo total de este algoritmo fue de: {total_elapsed_time} segundos")

# Se concluye el proceso MPI
MPI.Finalize()
