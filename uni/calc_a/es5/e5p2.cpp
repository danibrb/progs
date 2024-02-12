// Per passare un vettore ad una funzione occorre sempre passare il puntatore al vettore
#include <iostream>
using namespace std;
double vsum(int ndat, double *dat)
{
    int i;
    double sum = 0;
    for (i = 0; i < ndat; i++)
        sum += dat[i];
    return sum;
}
int main()
{
    int i, np = 10;
    double points[10];
    for (i = 0; i < np; i++)
    {
        cout << "Valore di points[" << i << "]: ";
        cin >> points[i];
    }
    cout << "La somma delle componenti vale " << vsum(np, points) << endl;

    return 0;
}