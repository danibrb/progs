// Calcolo dei parametri della retta che meglio approssima una serie di dati speriementali
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    int ndat;
    ifstream inFile;
    string filename = "pendolo.dat";
    double *x = NULL;
    double *sx = NULL;
    double *y = NULL;
    double *sy = NULL;
    double S0 = 0, Sx = 0, Sy = 0, Sxy = 0, Sxx = 0, den;
    double a, b, sa, sb;
    // apro il file e salvo i dati negli array
    inFile.open(filename.c_str());
    if (!inFile)
    {
        cout << "Errore nell'apertura del file" << endl;
    }
    else
    {
        inFile >> ndat; // il primo valore contiene il numero di prove
        // alloco dinamicamente i vettori
        x = new double[ndat];
        sx = new double[ndat];
        y = new double[ndat];
        sy = new double[ndat];

        for (int i = 0; i < ndat; ++i)
        {
            inFile >> x[i] >> sx[i] >> y[i] >> sy[i];
            // cout<< sy[i]<<endl;
        }
        inFile.close();
        // elaborazione dati
        for (int i = 0; i < ndat; i++)
        {
            S0 += 1 / (sy[i] * sy[i]);
            Sx += x[i] / (sy[i] * sy[i]);
            Sy += y[i] / (sy[i] * sy[i]);
            Sxy += (x[i] * y[i]) / (sy[i] * sy[i]);
            Sxx += (x[i] * x[i]) / (sy[i] * sy[i]);
        }
        den = Sxx * S0 - Sx * Sx;
        a = (Sxy * S0 - Sx * Sy) / den;
        b = (Sy * Sxx - Sx * Sxy) / den;
        sa = sqrt(S0 / den);
        sb = sqrt(Sxx / den);

        // stampo risultati
        cout << "a: " << a << " +/- " << sa << endl;
        cout << "b: " << b << " +/- " << sb << endl;

        // libero la memoria
        delete[] x;
        delete[] sx;
        delete[] y;
        delete[] sy;
    }
}