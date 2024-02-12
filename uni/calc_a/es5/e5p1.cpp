/*#include <iostream>
using namespace std;
void hello()
{
    cout << "Questa e' la mia prima funzione" << endl;
}
int main()
{
    hello();
    return 0;
}
Proviamo ora a passare un parametro alla funzione :
#include <iostream>
    using namespace std;
void sum(double a, double b)
{
    double c;
    c = a + b;
    cout << "La somma vale " << c << endl;
}
int main()
{
    double v1, v2;
    cout << "Valore di v1:";
    cin >> v1;
    cout << "Valore di v2:";
    cin >> v2;
    sum(v1, v2);
    return 0;
}
Proviamo ora ad utilizzare il valore di ritorno della funzione
#include <iostream>
    using namespace std;
double sum(double, double); // prototipo della funzione
int main()
{
    double v1, v2;
    cout << "Valore di v1:";
    cin >> v1;
    cout << "Valore di v2:";
    cin >> v2;
    cout << "La somma di v1 e v2 vale " << sum(v1, v2) << endl;
    return 0;
}
double sum(double a, double b)
{
    double c;
    c = a + b;
    return c;
}
Vediamo ora come modificare il parametro passato alla funzione(passaggio del puntatore)
#include <iostream>
    using namespace std;
void sum(double, double, double *); // prototipo della funzione
int main()
{
    double v1, v2, v;
    cout << "Valore di v1:";
    cin >> v1;
    cout << "Valore di v2:";
    cin >> v2;
    sum(v1, v2, &v);
    cout << "La somma di v1 e v2 vale " << v << endl;
    return 0;
}
void sum(double a, double b, double *c)
{
    *c = a + b;
}
Un 'altra maniera, esclusiva del C++, per modificare un parametro è passarlo per "referenza" senza l' aiuto del
    puntatore
#include <iostream>
    using namespace std;
void sum(double, double, double &);
int main()
{
    double v1, v2, v;
    cout << "Valore di v1:";
    cin >> v1;
    cout << "Valore di v2:";
    cin >> v2;
    sum(v1, v2, v);
    cout << "La somma di v1 e v2 vale " << v << endl;
    return 0;
}
void sum(double a, double b, double &c)
{
    c = a + b;
}
*/