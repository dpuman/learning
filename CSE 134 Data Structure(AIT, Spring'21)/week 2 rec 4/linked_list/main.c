#include <stdio.h>
#include <stdlib.h>
typedef struct Info
{
    int age;
    struct Info *next;
} Info;

int main()
{
    Info *ptr1, *ptr2;
    ptr1 = (Info *)malloc(sizeof(Info));
    ptr2 = (Info *)malloc(sizeof(Info));

    ptr1->age = 10;
    ptr2->age = 20;

    ptr1 -> next= ptr2;
    ptr2 -> next= NULL;

    printf("BLOCK A PTR1 %d\n",ptr1 ->age);
    printf("BLOCK B PTR2 %d\n",ptr1 -> next ->age);
//    printf("BLOCK B PTR2 %d\n",ptr2 ->age);


    return 0;
}
