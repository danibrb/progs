/*scrivere programma che Legga da terminale il nome del file da leggere.
Legga dal file tutti i numeri reali (senza sapere quanto vale n) salvandoli in un vettore.
Calcoli media (<x>), varianza (s2), varianza empirica (sN2), deviazione standard s, deviazione
standard adattata (sN) ed errore standard e*/

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

double media(double arr[], int dim);
double varianza(double arr[], int dim);

int main()
{
    const int NMAX = 100;
    int ndat;
    double x[NMAX];
    double mean, sigma2, sigma;
    double sn2, sn, err;
    ifstream file;
    ofstream fileout;
    string filename = "esempio.dat";
    string foutname = "risultati.dat";
    // cout << "inserisci il nome del file: ";
    // cin >> filename;
    file.open(filename.c_str()); // Conversione stringa C++ -> stringa C
    if (file)                    // controllo se file esiste
    {
        ndat = 0;
        while (file) // prelevo i dati
        {
            if (ndat < NMAX)
                file >> x[ndat++];
            else
            {
                cout << "array troppo piccolo!" << endl;
                return -1;
            }
        }
        ndat--;
        file.close(); // chiudo il file di origine
        // elaborazione dati
        mean = media(x, ndat);
        sigma2 = varianza(x, ndat);
        sigma = sqrt(sigma2);
        sn2 = sigma2 * (ndat / (ndat - 1));
        sn = sqrt(sn2);
        err = sn / sqrt(ndat);
        cout << "media: " << mean << endl;
        cout << "varianza: " << sigma2 << endl;
        cout << "varianza empirica: " << sn2 << endl;
        cout << "deviazione standard: " << sigma << endl;
        cout << "deviazione standard adattata: " << sn << endl;
        cout << "errore standard: " << err << endl;
        // scrittura su file
        fileout.open(foutname.c_str());
        if (fileout)
        {
            fileout << "media: " << mean << endl;
            fileout << "varianza: " << sigma2 << endl;
            fileout << "varianza empirica: " << sn2 << endl;
            fileout << "deviazione standard: " << sigma << endl;
            fileout << "deviazione standard adattata: " << sn << endl;
            fileout << "errore standard: " << err << endl;
            fileout.close();
        }
        else
        {
            cout << "errore nell'apertura del file!" << endl;
            return -2;
        }
    }
    else
    {
        cout << "errore nell'apertura del file!" << endl;
        return -2;
    }
    return 0;
}

double media(double arr[], int dim)
{
    double mean = 0;
    for (int i = 0; i < dim; i++)
        mean += arr[i];
    return mean / dim;
}

double varianza(double arr[], int dim)
{
    double m = 0, m2 = 0, sigma2;
    for (int i = 0; i < dim; i++)
    {
        m += arr[i];
        m2 += arr[i] * arr[i];
    }
    m /= dim;
    m2 /= dim;
    sigma2 = m2 - m * m;
    return sigma2;
}
