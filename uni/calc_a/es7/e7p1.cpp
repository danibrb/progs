// Esempio di utilizzo delle librerie grafiche: disegno di N punti date i vettori di coordinate x e y.
#include <iostream>
#include <TCanvas.h>
#include <TGraphErrors.h>
#include <TApplication.h>
using namespace std;

TApplication app("gui", 0, NULL);
int main()
{
    int ndat = 5;
    double x[5] = {0.0, 1.0, 2.0, 3.0, 4.0};
    double y[5] = {0.1, 0.3, 0.5, 0.4, 0.6};
    double ex[5] = {0.0, 0.0, 0.0, 0.0, 0.0};
    double ey[5] = {0.05, 0.05, 0.05, 0.05, 0.05};
    TCanvas c;                           // Crea la finestra grafica
    TGraphErrors gr(ndat, x, y, ex, ey); // Crea il grafico
    gr.Draw("AP");                       // Disegna il grafico calcolando automaticamente
    // gli assi (A) e disegnando punti (P)
    app.Run(true); // Attiva l'editor grafico
    c.Close();     // Chiude la finestra
    return 0;
}