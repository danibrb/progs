// Inserito da terminale un numero intero si termini se questo è primo.
#include <iostream>

using namespace std;
main()
{
    int num;
    cout << "inserisci un numero " << endl;
    cin >> num;
    for (int i = num / 2; i > 1; i--)
        if (num % i == 0)
        {
            cout << "il numero " << num << " non e' primo" << endl;
            return 1;
        }
    cout << "il numero " << num << " e' primo" << endl;
    return 0;
}