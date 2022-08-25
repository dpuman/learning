#include <stdio.h>
#include <stdlib.h>
// ARRAY DELETE
int main()
{
    int a[] = {1, 2, 3, 4, 5, 6}, b, *p, *q;

    b = 10;
    // address of b to p
    p = &b;
    // base address of a to q
    q = a;

    printf("%d \n", *p);
    printf("Address of b: %p \n", &b);
    printf("Address of b: %p \n", p);
    printf("Address of pointer p: %p \n", *p);

    // Array's name itself is a pointer which has the base value of the array

    printf("%d \n", a[2]);
    printf("%d \n", *(a + 2));
    printf("%d \n", *(q + 2));
    // A[2]==*(a+2) so, a[i]=*(a+i)
    // So we can also write *(i+a)==i[a]

    printf("%d \n", 2 [a]);

    printf("a:  %p \n", a);
    printf("&a:  %p \n", &a);
    // but
    // to next address
    printf("a + 1:  %p \n", a + 1);
    // to whole array  address +1
    printf("&a + 1:  %p \n", &a + 1);

    printf("*a + 1:  %d \n", *a + 1);
    printf("*(a + 1):  %d \n", *(a + 1));

    // Can we do these
    printf("a + 1:  %p \n", a + 1);
    // Cant do arithmetic operations
    // printf("a + 1:  %p \n", (a * 2));
    // printf("a + 1:  %p \n", (a / 2));

    return 0;
}