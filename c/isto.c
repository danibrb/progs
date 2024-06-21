#include <stdio.h>

#define R 5
#define C 4

// void stampa(char m[][C], int r, int c);
int main()
{
    int a[4] = {3, 2, 5, 1};
    char m[R][C];
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (a[j] % (R - i) == 0)
            {
                m[i][j] = '*';
                a[j]--;
            }
            else
                m[i][j] = ' ';
            printf("%c", m[i][j]);
        }
        printf("\n");
    }
    // stampa(m, R, C);
}

/*
void stampa(char m[][C], int r, int c)
{
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; i < c; j++)
        {
            printf("%c", m[i][j]);
        }
        printf("\n");
    }
}

*/