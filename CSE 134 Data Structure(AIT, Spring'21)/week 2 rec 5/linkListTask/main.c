#include <stdio.h>
#include <stdlib.h>
typedef struct Info
{
    int age;
    struct Info *next;
} Info;
int main()
{
    Info *ptr1, *ptr2, *ptr3;
    ptr1 = (Info *)malloc(sizeof(Info));
    ptr2 = (Info *)malloc(sizeof(Info));
    ptr3 = (Info *)malloc(sizeof(Info));

    ptr1->age = 10;
    ptr2->age = 20;
    ptr3->age = 30;

    ptr1->next = ptr2;
    ptr2->next = ptr3;
    ptr3->next = NULL;

    printf("BLOCK A PTR1 %d\n", ptr1->age);
    printf("BLOCK B PTR2 %d\n", ptr1->next->age);
    printf("BLOCK C PTR2 %d\n", ptr2->next->age);
    return 0;
}
