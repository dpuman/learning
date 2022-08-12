#include <stdio.h>
#include <stdlib.h>

typedef struct Info{
int age;
float height;
}Info;

int main()
{
    Info arr[10];
    arr[0].age=10;
    arr[0].height=10.5;

//    scanf("%d",&arr[0].age);

    printf("Hello world!\n");
    return 0;
}
