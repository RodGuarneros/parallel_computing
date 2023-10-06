from mpi4py import MPI
import time

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define the message to be sent (only process 0 sends messages)
if rank == 0:
    message = "Hello, I'm process 0"
else:
    message = None

# Start timing
start_time = time.time()

# Create a list to store messages received by each process
received_messages = []

# Perform the chained send and receive of messages
for i in range(1, size):
    if rank == i:
        received_message = comm.recv(source=i - 1)
        received_messages.append(received_message)
    elif rank == i - 1:
        comm.send(message, dest=i)

# End timing
end_time = time.time()

# Calculate and print the elapsed time (total time across all processes)
total_elapsed_time = comm.reduce(end_time - start_time, op=MPI.SUM, root=0)

# Gather received messages from all processes
all_received_messages = comm.gather(received_messages, root=0)

# Print rank, total elapsed time, and received messages for each process
for i in range(size):
    if rank == i:
        print(f"Process {rank} took {total_elapsed_time:.6f} seconds")
        print(f"I'm process {rank} and I received: {all_received_messages}")

# Finalize MPI
MPI.Finalize()
