#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, *p;
    p = &a;
    *p = 10;
    a++;
    *p++;
    printf("%d\n", a);
    return 0;
}
