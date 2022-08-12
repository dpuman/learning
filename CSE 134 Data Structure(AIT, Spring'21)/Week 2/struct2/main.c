#include <stdio.h>
#include <stdlib.h>
// to use shortcut struct
// SI =struct Info

typedef struct Info
{
    int age;
    float height;
} Info;

int main()
{
    int a;
    Info b, c;
    b.age = 25;
    b.height = 10.2;
    printf("AGE %d\n", b.age);
    printf("Height %f\n", b.height);
    return 0;
}
