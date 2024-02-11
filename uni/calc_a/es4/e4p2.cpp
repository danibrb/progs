// Allocazione dinamica di un vettore:
#include <iostream>
using namespace std;

main()
{
    double *p = NULL;
    int n, i;
    cout << "Inserisci la dimensione del vettore " << endl;
    cin >> n;
    p = new double[n];
    cout << "Inserisci le " << n << " componenti del vettore " << endl;
    for (i = 0; i < n; i++)
    {
        cin >> p[i];
    }
    cout << "Puntatore alla prima componente " << p << endl;

    cout << "Componenti del vettore ";
    for (i = 0; i < n; i++)
    {
        cout << " " << p[i];
    }
    cout << endl;
    delete[] p;
}