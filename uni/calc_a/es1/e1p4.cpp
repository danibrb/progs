// calcolo lato del quadrato data l'area
#include <iostream>
#include <cmath>
using namespace std;
main()
{
    double lato, area;
    cout << "dammi l'area del quadrato " << endl;
    cin >> area;
    if (area > 0)
    {
        lato = sqrt(area);
        cout << "il lato del quadrato vale: " << lato << endl;
    }
    else
        cout << "area negativa" << endl;
}