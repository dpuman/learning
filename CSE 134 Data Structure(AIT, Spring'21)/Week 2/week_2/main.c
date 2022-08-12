#include <stdio.h>
#include <stdlib.h>

void Test(int *q){
    *q=10;
    return;
}

int main()
{
    int a, *p;
    p=&a;

    *p=8;
    printf("a bfr test %d\n",a);
    Test(&a);
    printf("a aftr test %d\n",a);

    return 0;
}
