#include <stdio.h>
#include <stdlib.h>
void DISPALY(char name[])
{
}

int main()
{

    int *p, n = 10, i;
    p = (int *)malloc(n * sizeof(int)); // here we allocate memory in heap
    for (i = 0; i < n; i++)
    {
        p[i] = i;
    }
    for (i = 0; i < n; i++)
    {
        printf("%d\n", p[i]);
    }
    return 0;
}
