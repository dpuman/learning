#include <stdio.h>
#include <stdlib.h>

typedef struct Data
{
    int age;
    struct Data *next;
    struct Data *prev;
} Data;

Data *head, *tail;

void insert_at_first(int a)
{
    Data *temp = (Data *)malloc(sizeof(Data));
    temp->age = a;
    temp->next = NULL;
    temp->prev = NULL;

    if (head == NULL)
    {
        head = temp;
        tail = temp;
        return;
    }

    temp->next = head;
    head->prev = temp;
    head = temp;

    return;
}

void insert_at_last(int a)
{
    Data *temp = (Data *)malloc(sizeof(Data));
    temp->age = a;
    temp->next = NULL;
    temp->prev = NULL;

    if (head == NULL)
    {
        head = temp;
        tail = temp;
        return;
    }

    tail->next = temp;
    temp->prev = tail;
    tail = temp;
}

void insert_at_nth(int v, int n)
{
    Data *temp_head = head;

    Data *new_node = (Data *)malloc(sizeof(Data));
    new_node->age = v;
    new_node->next = NULL;
    new_node->prev = NULL;

    if (n == 1)
    {
        new_node->next = head;
        temp_head->prev = new_node;
        head = new_node;
        return;
    }

    n -= 2;
    while (n--)
    {
        if (temp_head->next == NULL || head->next == NULL)
        {
            temp_head->next = new_node;
            new_node->prev = temp_head;
            tail = new_node;
            return;
        }
        temp_head = temp_head->next;
    }

    new_node->next = temp_head->next;
    temp_head->next->prev = new_node;

    temp_head->next = new_node;
    new_node->prev = temp_head;
}

void delete_by_value(int val)
{
    Data *temp_head = head;

    while (temp_head->age != val)
    {
        temp_head = temp_head->next;
        if (temp_head == NULL)
            break;
    }
    // cant find the value
    if (temp_head == NULL)
    {
        return;
    }

    // In case of single node
    if (head == tail)
    {
        free(head);
        head = tail = NULL;
        return;
    }

    // first node
    if (temp_head == head)
    {
        head = temp_head->next;
        temp_head->next->prev = NULL;
        free(temp_head);
        return;
    }

    // last node
    if (temp_head->next == NULL)
    {
        temp_head->prev->next = NULL;
        tail = temp_head->prev;
        free(temp_head);
        return;
    }

    temp_head->prev->next = temp_head->next;
    temp_head->next->prev = temp_head->prev;
    free(temp_head);
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
    head = tail = NULL;

    insert_at_first(2);
    insert_at_first(1);
    insert_at_last(3);
    insert_at_last(4);
    insert_at_last(5);
    insert_at_last(6);
    // insert_at_last(1);

    insert_at_nth(20, 4);
    delete_by_value(3);
    display();

    return 0;
}
