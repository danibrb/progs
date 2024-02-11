// Introduzione delle matrici
#include <iostream>
using namespace std;
main()
{

    // Matrice allocata staticamente
    double x[2][3] = {0.0, 3.0, 2.0,
                      1.0, 4.0, 1.0};
    cout << " Valori della matrice: " << endl;
    for (int j = 0; j < 2; j++)
    {
        for (int i = 0; i < 3; i++)
        {
            cout << x[j][i] << " ";
        }
    }
    cout << endl;
    // Matrice allocata dinamicamente
    int nrow, ncol;
    double **matrix;
    cout << "Inserisci il numero di righe e di colonne" << endl;
    cin >> nrow >> ncol;
    matrix = new double *[nrow];
    for (int i = 0; i < nrow; i++)
    {
        matrix[i] = new double[ncol];
    }
    cout << "Inserisci il valore degli elementi della matrice " << endl;
    for (int i = 0; i < nrow; i++)
    {
        for (int j = 0; j < ncol; j++)
        {
            cout << " elemento [" << i << "][" << j << "]" << endl;
            cin >> matrix[i][j];
        }
    }
    cout << " Valori della matrice: " << endl;
    for (int j = 0; j < nrow; j++)
    {
        for (int i = 0; i < ncol; i++)
        {
            cout << matrix[j][i] << " ";
        }
    }
    cout << endl;
    for (int i = 0; i < nrow; i++)
    {
        delete[] matrix[i];
    }
    delete[] matrix;
}