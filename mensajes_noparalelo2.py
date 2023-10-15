import time

num_processes = int(input("Introduzca el numero de procesos (entre 2 y el número de nucleos): "))

start_time = time.time()

received_message = "Este mensaje es para"
received_initial = "Hola, soy el proceso 0"

print(received_initial)

for i in range(1, num_processes):
    if i == 1:
        received_message = received_initial
        print(f"Son el proceso 1 y recibi el mensaje del proceso 0: {received_message}")
    else:
        message = received_message
        received_message = f"{message}"
        print(f"Yo soy el proceso {i} y recibi el mensaje del proceso {i - 1}: {received_message}")

end_time = time.time()

total_elapsed_time = end_time - start_time

print(f"El tiempo total de ejecución es de: {total_elapsed_time:.15f} segundos")
