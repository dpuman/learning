#include <stdio.h>
#include <stdlib.h>

typedef struct Info
{
    int age;
    float height;
} Info;

int main()
{
    Info arr[1];
    for(int i=0;i<1;i++){

    scanf(" %d", &arr[0].age);
    scanf(" %d", &arr[0].height);
    }


    printf("%d", arr[0].age);
    return 0;
}
