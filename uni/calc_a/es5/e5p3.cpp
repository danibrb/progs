// Strutturare con funzioni il programma precedentemente preparato per il calcolo delle media,
// varianza, deviazione standard, errore standard.
#include <iostream>
using namespace std;

double vsum(int ndat, double *dat);
double mean(int ndat, double *dat);
double var(int ndat, double *dat);
double dev(int ndat, double *dat);
double err(int ndat, double *dat);

int main()
{
    int i, np = 10;
    double points[10];
    for (i = 0; i < np; i++)
    {
        // cout << "Valore di points[" << i << "]: ";
        // cin >> points[i];
        points[i] = i;
    }
    cout << "La somma delle componenti vale " << vsum(np, points) << endl;
    cout << "La media vale " << mean(np, points) << endl;
    cout << "La varianza vale " << var(np, points) << endl;

    return 0;
}

double vsum(int ndat, double *dat)
{
    double sum = 0;
    for (int i = 0; i < ndat; i++)
        sum += dat[i];
    return sum;
}

double mean(int ndat, double *dat)
{
    double sum = 0;
    for (int i = 0; i < ndat; i++)
        sum += dat[i];
    return sum / ndat;
}

double var(int ndat, double *dat)
{
    double mean = 0, mean2 = 0;
    for (int i = 0; i < ndat; i++)
    {
        mean += dat[i];
        mean2 += dat[i] * dat[i];
    }
    mean /= ndat;
    mean2 /= ndat;
    return mean2 - mean * mean;
}