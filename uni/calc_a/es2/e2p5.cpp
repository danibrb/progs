// determinare i primi venti numeri primi
#include <iostream>
#include <stdbool.h>

bool isprime(int num);

using namespace std;

main()
{
    const int dim = 100;
    // int arr[dim]={1};
    int n = 1;
    cout << "i primi " << dim << " numeri primi sono" << endl;
    for (int i = 0; i < dim;)
    {
        if (isprime(n) == true)
        {
            cout << n << " ";
            i++;
        }
        n++;
    }
}

bool isprime(int num)
{
    for (int i = num / 2; i > 1; i--)
        if (num % i == 0)
        {
            // cout << "il numero " << num << " non e' primo" << endl;
            return false;
        }
    // cout << "il numero " << num << " e' primo" << endl;
    return true;
}