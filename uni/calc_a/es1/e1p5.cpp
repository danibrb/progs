// calcolo soluzioni equazione di secondo grado
#include <iostream>
#include <cmath>
using namespace std;
main()
{
    double a, b, c, delta, x1, x2;
    cout << "dammi i coefficienti dell'equazione di secondo grado ax^2+bx+c=0 " << endl;
    cin >> a >> b >> c;
    if (a == 0)
        if (b == 0)
            if (c == 0)
                cout << "indeterminata" << endl;
            else
                cout << "impossibile" << endl;
        else
        {
            x1 = -b / c;
            cout << "la soluzione e' " << x1 << endl;
        }
    else
    {
        delta = b * b - 4 * a * c;
        if (delta < 0)
            cout << "no soluzioni reali" << endl;
        else if (delta == 0)
        {
            x1 = -b / (2 * a);
            cout << "la soluzione e' " << x1 << endl;
        }
        else
        {
            delta = sqrt(delta);
            x1 = (-b + delta) / (2 * a);
            x2 = (-b - delta) / (2 * a);
            cout << "le soluzioni sono: " << x1 << " " << x2 << endl;
        }
    }
}