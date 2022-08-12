#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, *p;
    a = 10;
    // scanf('%d', &a);
    printf("%d\n", &a);
    printf("%d\n", a);
    printf("%x\n", &a);
    p = &a;
    printf("%x\n", p);
    return 0;
}
