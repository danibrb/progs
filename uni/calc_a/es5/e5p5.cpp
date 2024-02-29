// Elenco del telefono

#include <iostream>
#include <string>
#include <fstream>
using namespace std;
// ricerca della stringa key nel vettore di stringhe el:
// gli indici delle stringhe trovate nel vettore el sono salvate
// nel vettore di interi index
bool find(string *el, int nel, string key, int **index, int &nindex)
{
    // calcolo del numero di elementi
    nindex = 0;
    for (int i = 0; i < nel; i++)
    {
        if (el[i] == key)
            nindex++;
    }
    if (nindex == 0)
        return false;
    // allocazione
    *index = new int[nindex];

    // riempimento del vettore index
    int m = 0;
    for (int i = 0; i < nel; i++)
    {
        if (el[i] == key)
            (*index)[m++] = i;
    }
    return true;
}
int main()
{
    ifstream f("elenco.dat");
    if (!f)
        return -1;
    // lettura dei dati da file
    int n;
    f >> n;
    string *nome = new string[n];
    string *cnome = new string[n];
    int *num = new int[n];
    for (int i = 0; i < n; i++)
    {
        f >> num[i] >> cnome[i] >> nome[i];
    }
    f.close();
    string ckey;
    while (1)
    {
        int *ind, nind;
        cout << "inserisci il cognome (break per fermarsi)" << endl;
        cin >> ckey;
        if (ckey == "break")
            break;
        if (find(cnome, n, ckey, &ind, nind))
        {
            for (int j = 0; j < nind; j++)
            {
                cout << cnome[ind[j]] << " " << num[ind[j]] << endl;
            }
            delete[] ind; // e' necessario disallocare ind prima di richiamare find
        }
        else
        {
            cout << "nome non trovato " << endl;
        }
    }
    delete[] nome;
    delete[] cnome;
    delete[] num;
}