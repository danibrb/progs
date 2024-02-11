// allocazione dinamica vettori

#include <iostream>

using namespace std;
main()
{
    int dim;
    double *vet;
    cout << "inserisci dimensione vettore: " << endl;
    cin >> dim;
    // alloco dinamicamente
    vet = new double[dim];
    // controllo se c'e' spazio in memoria
    if (vet != NULL)
    {
        for (int i = 0; i < dim; i++)
        {
            vet[i] = i;
            cout << vet[i] << " ";
        }
    }
    // libero la memoria finito di usare il vettore
    delete[] vet;
}