#include <stdio.h>
#include <stdlib.h>
// ARRAY DELETE
int main()
{
    int a[3], *q, i;
    q = a;

    for (i = 0; i < 3; i++)
    {
        // scanf("%d", &a[i]);
        // scanf("%d", a + i);
        // scanf("%d", q + i);
        scanf("%d", i + q);
    }

    for (i = 0; i < 3; i++)
    {
        printf("%d", a[i]);
        printf("%d", i[a]);
        printf("%d", *(a + i));
        printf("%d", *(q + i));
    }

    return 0;
}