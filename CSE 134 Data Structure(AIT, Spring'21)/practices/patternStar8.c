#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, j, n = 5, number = 1;

    for (i = 0; i <= n; i++)
    {
        for (j = 1; j <= (n - i); j++)
        {
            printf(" ");
        }
        for (int k = 0; k < (2 * i - 1); k++)
        {
            printf("*");
        }

        printf("\n");
    }

    for (i = n - 1; i > 0; i--)
    {
        for (j = 0; j < (n - i); j++)
        {
            printf(" ");
        }
        for (int k = 0; k < (i * 2 - 1); k++)
        {
            printf("*");
        }

        printf("\n");
    }
    return 0;
}