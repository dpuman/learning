#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, j, n = 5;

    for (int i = n; i >= 1; i--)
    {
        for (int j = 1; j <= i; j++)
        {
            printf("*");
        }
        printf("\n");
    }

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (i + j <= n)
            {
                printf(" ");
            }
            else
            {
                printf("*");
            }
            printf("\n");
        }
    }

    return 0;
}