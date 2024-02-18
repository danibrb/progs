// Si consideri un file di dati punti.dat contenente le coordinate di vettori nel piano nel formato
// calcolare il modulo di ciascun vettore
// trovare i vettori con modulo massimo e minimo e stamparne le coordinate.

// TODO: faccio la versione easy, senza generalizzare il vettore a n-componenti

#include <iostream>
#include <fstream>
#include <cmath>
#include <cfloat>
#include <limits>

using namespace std;

#define ncomp 2 // fisso vettore a due componenti

void stampa(double **mat, int numRows, int numCols, int row);
double modulo(double **mat, int numRows, int numCols, int row);
void minmax(double **mat, int numRows, int numCols, bool mode);

int main()
{
    // apro il file
    ifstream f("punti.dat");
    if (!f) // verifico corretta apertura
        return -1;

    // Matrice allocata dinamicamente
    int nvet;
    //  lettura dei dati da file
    f >> nvet;
    double **vet;
    vet = new double *[nvet];
    for (int i = 0; i < nvet; i++)
    {
        vet[i] = new double[ncomp];
    }
    // carico i dati
    for (int i = 0; i < nvet; i++)
        for (int j = 0; j < ncomp; j++)
            f >> vet[i][j];
    f.close();
/*
    // stampo i moduli
    for (int i = 0; i < nvet; i++)
    {
        cout << modulo(vet, nvet, ncomp, i) << endl;
    }
*/
    minmax(vet, nvet, ncomp, 0);
    minmax(vet, nvet, ncomp, 1);

    //  libero la memoria
    for (int i = 0; i < nvet; i++)
        delete[] vet[i];
    delete[] vet;
}

void stampa(double **mat, int numRows, int numCols, int row)
{
    for (int col = 0; col < numCols; ++col)
    {
        cout << mat[row][col] << " ";
    }
    cout << endl;
}

double modulo(double **mat, int numRows, int numCols, int row)
{
    if (row < 0 || row >= numRows)
    {
        cout << "Invalid row index." << endl;
        return -1;
    }
    double mod = 0;
    for (int i = 0; i < numCols; i++)
    {
        mod += mat[row][i] * mat[row][i];
    }
    return sqrt(mod);
}

void minmax(double **mat, int numRows, int numCols, bool mode){ // 0 min 1 max
    double min=DBL_MAX, max=0, mod;
    int imin, imax;
    for (int i = 0; i < numRows; i++)
    {
        mod=modulo(mat, numRows, numCols,i);
        if(mode==0 && mod<min){
            min=mod;
            imin=i;
        }
        if(mode==1 && mod>max){
            max=mod;
            imax=i;
        }
    }
    if(mode==0)
        cout<<"moulo minimo: " << min <<" indice: " << imin <<endl;
    if(mode==1)
        cout<<"moulo massimo: " << max <<" indice: " << imax <<endl;
    
}