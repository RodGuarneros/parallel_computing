#include <iostream>
#include <cmath>
#include <chrono>

using namespace std;
using namespace std::chrono;

int main(int argc, char *argv[])
{
    int n;
    cin >> n;

    double PI25DT = 3.141592653589793238462643;
    double h = 1.0 / static_cast<double>(n);
    double sum = 0.0;

    // Start the timer
    auto start_time = high_resolution_clock::now();

    for (int i = 1; i <= n; i++) {
        double x = h * (static_cast<double>(i) - 0.5);
        sum += (4.0 / (1.0 + x * x));
    }

    double pi = sum * h;

    // Stop the timer
    auto stop_time = high_resolution_clock::now();

    auto duration = duration_cast<microseconds>(stop_time - start_time);

    cout << "La aproximacion del valor de PI es: " << pi << ", con un error de " << fabs(pi - PI25DT) << endl;
    cout << "Tiempo de ejecucion: " << duration.count() / 1000000.0 << " segundos" << endl;

    return 0;
}

