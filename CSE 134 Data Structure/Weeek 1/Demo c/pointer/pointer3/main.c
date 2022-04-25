#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,*p;
    a=10,
    p=&a;
    //a ar address a value dia overwrite
    *p=50;
    printf("%d\n",a);
    return 0;
}
