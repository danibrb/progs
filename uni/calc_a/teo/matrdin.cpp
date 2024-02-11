// allocazione dinamica matrici

#include <iostream>

using namespace std;
main()
{
    int nrow, ncol;
    double **matrix;
    cout << "numero righe e colonne ";
    cin >> nrow >> ncol;
    // allocazione dinamica
    matrix = new double *[nrow];
    for (int i = 0; i < nrow; i++)
    {
        matrix[i] = new double[ncol];
    }

    // utilizzo matrice
    for (int i = 0; i < nrow; i++)
    {
        for (int j = 0; j < ncol; j++)
        {
            matrix[i][j] = i * j;
        }
    }

    for (int i = 0; i < nrow; i++)
    {
        for (int j = 0; j < ncol; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    // libero memoria
    for (int i = 0; i < nrow; i++)
        delete[] matrix[i];
    delete[] matrix;
}