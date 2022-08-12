#include <stdio.h>
#include <stdlib.h>

typedef struct Data
{
    int age;
    struct Data *next;
} Data;

Data *head;

void insert_at_first(int a)
{
    Data *temp = (Data *)malloc(sizeof(Data));
    temp->age = a;
    temp->next = NULL;

    temp->next = head;
    head = temp;

    return;
}

void display()
{
    Data *temp = head;
    while (temp != NULL)
    {
        printf("%d \n", temp->age);
        temp = temp->next;
    }
    return;
}

int main()
{
    head = NULL;

    insert_at_first(5);
    insert_at_first(7);
    insert_at_first(12);

    display();


    return 0;
}
