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

void insert_at_last(int a)
{
    Data *temp = (Data *)malloc(sizeof(Data));
    temp->age = a;
    temp->next = NULL;

    if (head == NULL)
    {
        head = temp;
        return;
    }

    Data *node = head;
    while (node->next != NULL)
    {
        node = node->next;
    }

    node->next = temp;
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

    insert_at_first(7);
    insert_at_first(12);
    insert_at_first(12);

    insert_at_last(30);

    display();

    return 0;
}
