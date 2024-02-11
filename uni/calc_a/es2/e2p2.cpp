// Creazione di un vettore, assegnazione e stampa condizionata
#include <iostream>
#include <cmath>
using namespace std;
main()
{
    const int dim = 100;
    int i;
    double arr[dim];

    // Ad ogni componente e' assegnata la radice quadrata dell'indice
    for (i = 0; i < dim; i++)
        arr[i] = sqrt(i);
    // Stampo solo le componenti del vettore con valore > 5
    i = 99;
    while (i > 0 && arr[i] > 5.)
    {
        cout << arr[i] << endl;
        i--;
    }
}