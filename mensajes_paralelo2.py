from mpi4py import MPI
import time

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Input the number of processes
if rank == 0:
    num_processes = int(input("Enter the number of processes (must be at least 2): "))
else:
    num_processes = None

# Broadcast the number of processes to all ranks
num_processes = comm.bcast(num_processes, root=0)

# Input the initial message (only process 0 inputs)
if rank == 0:
    initial_message = "Hola soy el proceso 0"
    print(initial_message)
else:
    initial_message = None

# Broadcast the initial message to all ranks
initial_message = comm.bcast(initial_message, root=0)

# Start timing
start_time = time.time()

# Perform the chained send and receive of messages


for i in range(1, num_processes):
    if rank == i:
        received_message = comm.recv(source=i - 1)
        print(f"Soy el proceso {rank} y he recibido el mensaje de {i - 1} y dice que 0 envio este mensaje: {received_message}")
    elif rank == i - 1:
        message = f"{initial_message}"
        comm.send(message, dest=i)

# End timing
end_time = time.time()

# Calculate and print the elapsed time (total time across all processes)
total_elapsed_time = comm.reduce(end_time - start_time, op=MPI.SUM, root=0)
print(total_elapsed_time)

# Finalize MPI
MPI.Finalize()

