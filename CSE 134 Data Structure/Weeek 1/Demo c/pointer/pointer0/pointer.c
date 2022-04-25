#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, *ptr;
    a = 10;
    printf("%x\n", &a);
    printf("%d\n", a);
    ptr = &a;
    printf("ptr hex %x\n", ptr);
    printf("ptr a v %d\n", *ptr);
    printf("A %d\n", a);

    return 0;
}