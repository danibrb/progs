// Leggere da file una matrice Temp (Nx5) contenente per i valori di temperatura registrati ogni giorno
// per N giorni (5 temperature per giorno) allocandola dinamicamente.
// Identificare il giorno con maggior scarto tra la temperatura minima e la temperatura massima.
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// double diff(double arr[], int dim);

int main()
{
    ifstream inFile;
    string filename = "temperature.dat";
    double deltamax = 0;
    int day;
    // Matrice allocata dinamicamente
    int nrow, ncol = 5;
    double **matrix;
    // apro il file e salvo i dati nella matrice
    inFile.open(filename.c_str());
    if (!inFile)
    {
        cout << "Errore nell'apertura del file" << endl;
    }
    else
    {
        inFile >> nrow;
        matrix = new double *[nrow];
        for (int i = 0; i < nrow; i++)
        {
            matrix[i] = new double[ncol];
        }
        // carico i dati
        for (int i = 0; i < nrow; i++)
            for (int j = 0; j < ncol; j++)
                inFile >> matrix[i][j];
        inFile.close();

        // elaboro i dati
        for (int i = 0; i < nrow; i++)
        {
            double min = matrix[i][0], max = matrix[i][0];
            for (int j = 0; j < ncol; j++)
            {
                if (matrix[i][j] > max)
                    max = matrix[i][j];
                if (matrix[i][j] < min)
                    min = matrix[i][j];
            }
            if (max - min > deltamax)
            {
                deltamax = max - min;
                day = i + 1;
            }
        }

        cout << " Valori della matrice: " << endl;
        for (int j = 0; j < nrow; j++)
        {
            for (int i = 0; i < ncol; i++)
            {
                cout << matrix[j][i] << " ";
            }
            cout << endl;
        }

        cout << "il " << day << " giorno ha avuto il maggior scarto" << endl;
        cout << "scarto: " << deltamax << endl;

        // libero la memoria
        for (int i = 0; i < nrow; i++)
            delete[] matrix[i];
        delete[] matrix;
    }
}

/*
double diff(double arr[], int dim){
    double min=arr[0], max=arr[0];
    for (int i = 0; i < dim; i++)
    {
        if(arr[i]>max)
            max=arr[i];
        if(arr[i]<min)
            min=arr[i];
    }
    return max-min;
}
*/