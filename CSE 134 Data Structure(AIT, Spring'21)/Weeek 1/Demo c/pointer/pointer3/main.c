#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, *p;
    a = 10,
    // a ar address p te
        p = &a;
    // a ar address a new value dia overwrite
    *p = 50;
    printf("%d\n", a);
    return 0;
}
