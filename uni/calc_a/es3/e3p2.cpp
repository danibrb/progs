// Lettura da un file contenente il numero di componenti di un vettore e i loro valori:

#include <iostream>
#include <fstream>
using namespace std;
main()
{
    ifstream inFile;
    int ndat;
    double val[30]; // attenzione la dimensione del vettore deve essere
    // sufficiente a contenere tutti i valore del file (controllate)
    inFile.open("esempio.dat");
    if (!inFile)
    {
        cout << "Errore nell'apertura del file" << endl;
    }
    else
    {
        inFile >> ndat;
        for (int i = 0; i < ndat; ++i)
        {
            inFile >> val[i];
        }
        inFile.close();
    }

    for (int i = 0; i < ndat; i++)
    {
        cout << val[i] << " ";
    }
}