#include <iostream>

void print1DArrayFrom2D(int **array2D, int numRows, int numCols, int row)
{
    if (row < 0 || row >= numRows)
    {
        std::cout << "Invalid row index." << std::endl;
        return;
    }

    for (int col = 0; col < numCols; ++col)
    {
        std::cout << array2D[row][col] << " ";
    }
    std::cout << std::endl;
}

int main()
{
    const int numRows = 3;
    const int numCols = 4;

    int **array2D = new int *[numRows];
    for (int i = 0; i < numRows; ++i)
    {
        array2D[i] = new int[numCols];
    }

    // Fill the 2D array with some values
    int value = 1;
    for (int i = 0; i < numRows; ++i)
    {
        for (int j = 0; j < numCols; ++j)
        {
            array2D[i][j] = value++;
        }
    }

    int rowToPrint = 1;
    print1DArrayFrom2D(array2D, numRows, numCols, rowToPrint);

    // Clean up the dynamically allocated memory
    for (int i = 0; i < numRows; ++i)
    {
        delete[] array2D[i];
    }
    delete[] array2D;

    return 0;
}