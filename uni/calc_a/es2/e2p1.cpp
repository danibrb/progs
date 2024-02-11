// Verifica delle divisibilità dell'intero i per l'intero j
#include <iostream>

using namespace std;
main()
{
    int i, j;
    cout << "inserisci due numeri interi " << endl;
    cin >> i >> j;
    if (i % j == 0)
        cout << "il numero " << i << " e' divisibile per " << j << endl;
    else
        cout << "il numero " << i << " non e' divisibile per " << j << endl;
}