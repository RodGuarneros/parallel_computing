#include <iostream>
#include <cmath>
#include <cstdlib>
#include <mpi.h>

using namespace std;

int main(int argc, char *argv[]) {
    int n, precision;
    double PI25DT = 3.141592653589793238462643;
    double h, local_sum, global_sum, pi;

    // Initialize MPI
    MPI_Init(&argc, &argv);

    // Get the size and rank of the communicator
    int comm_size, comm_rank;
    MPI_Comm_size(MPI_COMM_WORLD, &comm_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &comm_rank);

    if (comm_rank == 0) {
        // Process 0 reads the value of 'n' and 'precision' from the user
        cin >> n >> precision;
    }

    // Broadcast 'n' and 'precision' from process 0 to all other processes
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Bcast(&precision, 1, MPI_INT, 0, MPI_COMM_WORLD);

    h = 1.0 / static_cast<double>(n);
    local_sum = 0.0;

    // Calculate the local sum for this process
    for (int i = comm_rank + 1; i <= n; i += comm_size) {
        double x = h * (static_cast<double>(i) - 0.5);
        local_sum += (4.0 / (1.0 + x * x));
    }

    // Use MPI Reduce to combine local sums into the global sum
    MPI_Reduce(&local_sum, &global_sum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    // Print rank and size of each process
    cout << "Process " << comm_rank << " of " << comm_size << " says: ";
    cout << "Local sum: " << local_sum << endl;

    // Calculate PI on process 0
    if (comm_rank == 0) {
        pi = global_sum * h;
        // Apply precision factor to the result
        double precision_factor = pow(10.0, -precision);
        pi = round(pi / precision_factor) * precision_factor;
        cout << "La aproximacion del valor de PI es: " << pi << ", con un error de " << fabs(pi - PI25DT) << endl;
    }

    // Finalize MPI
    MPI_Finalize();

    return 0;
}
