/*Creare un array a 10 componenti e leggerne da terminale le componenti. Quindi:
calcolare la somma delle componenti e la media
calcolate la media dei quadrati delle componenti
stampare le componenti con valore minimo e massimo */

#include <iostream>
#include <cstdlib>
#include <time.h>
#include <cmath>
using namespace std;
main()
{
    const int dim = 1000;
    int lmin = 0, lmax = 100;
    int min = lmax, max = lmin;
    int i, somma = 0, somquad = 0;
    int arr[dim];

    srand(time(NULL));

    // Ad ogni componente e' assegnato un numero random
    for (i = 0; i < dim; i++)
    {
        arr[i] = rand() % (lmax - lmin + 1) + lmin; // non e' la scelta migliore!!
        // cout << arr[i] << " ";
        somma += arr[i];
        somquad += arr[i] * arr[i];
        if (arr[i] > max)
            max = arr[i];
        if (arr[i] < min)
            min = arr[i];
    }
    cout << "somma: " << somma << " media: " << somma / dim << " media quadrati: " << somquad / dim << endl;
    cout << "max: " << max << " min " << min << endl;
}