#include <stdio.h>
#include <stdlib.h>
typedef struct Data
{
    int age;
    struct Data *next;
} Data;

int main()
{
    Data *head, *temp;
    // BLOCK A
    head = (Data *)malloc(sizeof(Data));
    head->age = 5;
    // BLOCK B
    head->next = (Data *)malloc(sizeof(Data));
    head->next->age = 7;
    // BLOCK C
    head->next->next = (Data *)malloc(sizeof(Data));
    head->next->next->age = 11;

    head->next->next->next = NULL;

    temp = head;
    while (temp != NULL)
    {
        printf("%d", temp->age);
        temp = temp->next;
    }

    //    printf("BLOCK A  %d\n", head->age);
    //    printf("BLOCK B  %d\n", head->next->age);
    //    printf("BLOCK C  %d\n", head->next->next->age);
    return 0;
}
