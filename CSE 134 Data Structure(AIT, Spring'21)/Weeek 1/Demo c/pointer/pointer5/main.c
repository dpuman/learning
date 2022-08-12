#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, *p;
    p = &a;
    *p = 10;
    a++;

    printf("%x\n", p);
    *p++;
    printf("%x\n", p);

    printf("%d\n", a);
    return 0;
}
