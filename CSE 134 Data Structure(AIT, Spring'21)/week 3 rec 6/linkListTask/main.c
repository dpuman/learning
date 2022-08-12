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

    head = (Data *)malloc(sizeof(Data));
    head->age = 10;

    head->next = (Data *)malloc(sizeof(Data));
    head->next->age = 20;

    head->next->next = (Data *)malloc(sizeof(Data));
    head->next->next->age = 30;

    head->next->next->next = NULL;
    temp = head;

    for (temp;temp != NULL;temp = temp->next)
    {
        printf("%d", temp->age);

    }

    return 0;
}
