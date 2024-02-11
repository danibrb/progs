// Lettura di un file il cui nome è specificato da terminale
//  e di cui non si conosce, a priori, il numero di dati contenuti.

#include <fstream>
#include <iostream>
#include <string>
using namespace std;
main()
{
    int ndat;
    double x[100];
    ifstream file;
    string filename;
    cout << "Inserisci il nome del file " << endl;
    cin >> filename;
    file.open(filename.c_str()); // Conversione stringa C++ -> stringa C
    if (file)
    {
        ndat = 0;
        while (file)
        {
            if (ndat < 100)
                file >> x[ndat++];
            else
            {
                cout << "Array troppo piccolo !" << endl;
                return (0);
            }
        }
        ndat--;
        file.close();
        cout << ndat << endl;
        for (int i = 0; i < ndat; i++)
            cout << x[i] << " ";
        cout << endl;
    }
    else
    {
        cout << "Errore nell' apertura del file " << endl;
    }
}