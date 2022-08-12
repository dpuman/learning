#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, j, n = 5;
    for (i = 0; i <= n; i++)
    {
        for (j = 0; j <= i; j++)
        {
            printf("%d", i);
        }
        printf("\n");
    }
    return 0;
}