// Utilizzo delle stringhe: assegnazione, concatenazione, lunghezza della stringa,
// accesso ai singoli caratteri e confronto.
#include <iostream>
#include <string>

using namespace std;
main()
{
    string myString = "AAA";
    char a;
    // Concatenzione
    myString += "BB";
    cout << myString << endl;
    // Assegnazione tramite caratteri;
    myString[0] = 'a';
    myString[1] = 'b';
    a = 'c';
    myString[2] = a;
    cout << myString << endl;
    // Stampa dei singoli caratteri
    cout << "Inserisci la stringa: ";
    cin >> myString;
    for (int i = 0; i < myString.length(); i++)
    {
        cout << myString[i] << endl;
    }
    // Confronto di stringhe
    while (myString != "quit")
    {
        cout << "Inserisci la stringa: ";
        cin >> myString;
        cout << myString.length() << endl;
    }
}