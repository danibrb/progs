// Puntatori, operatori * e &.
#include <iostream>
using namespace std;
main()
{
    double a = 8.0, b = 4.0;
    double *p = NULL; // puntatore inizializzato a 0 (nessuna zona di memoria)
    p = &a;           // Faccio in modo che p punti alla locazione di memoria di a
    cout << "L'indirizzo di a e' " << p << endl;
    cout << "Il contenuto di a e' " << *p << endl;
    b = *p;   // Assegno a b il valore puntato da p
    *p = 5.0; // assegno alla casella di memoria puntato da p il valore 5.0
    cout << "Il valore di a e' " << a << endl;
    cout << "Il valore di b e' " << b << endl;
    double v[3] = {0.0, 1.0, 2.0};
    p = &v[0];
    cout << "L'indirizzo di v[0] e' " << p << endl;
    p = v;
    cout << "L'indirizzo di v e' " << p << endl;
    double *q = &v[1];
    cout << "Il valore della seconda componente e' " << *q << endl;
    cout << "Il valore della seconda componente e' " << *(p + 1) << endl;
}