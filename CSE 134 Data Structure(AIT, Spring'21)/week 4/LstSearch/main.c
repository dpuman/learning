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

void insert_at_nth(int v, int n)
{
    Data *temp = head;

    Data *node = (Data *)malloc(sizeof(Data));
    node->age = v;
    node->next = NULL;

    if (n == 1)
    {
        node->next = head;
        head = node;
        return;
    }

    n -= 2;
    while (n--)
    {
        if (temp->next == NULL || head->next == NULL)
        {
            temp->next = node;

            return;
        }
        temp = temp->next;
    }

    node->next = temp->next;
    temp->next = node;
}

void del_by_pos(int pos)
{

    Data *temp_head = head, *delete_block;

    if (pos == 1)
    {

        delete_block = head;

        head = head->next;

        free(delete_block);
        return;
    }

    pos -= 2;

    while (pos--)
    {
        temp_head = temp_head->next;
    }
    delete_block = temp_head->next;

    temp_head->next = delete_block->next;

    free(delete_block);

    return;
}

void del_by_val(int val)
{
    Data *temp_head = head, *delete_node;

    if (head->age == val)
    {
        printf("Inside IF temp %d \n", temp_head->age);
        printf("Inside IF  head %d \n", head->age);
        delete_node = head;
        head = head->next;
        free(delete_node);

        return;
    }

    while (temp_head->next->age != val)
    {
        printf("Inside while %d \n", temp_head->age);

        temp_head = temp_head->next;
    }
    printf("outside while %d \n", temp_head->age);

    delete_node = temp_head->next;
    temp_head->next = delete_node->next;

    free(delete_node);
    return;
}

void insert_a_node_after_seven_val_node(int val)
{
    Data *new_node, *temp_head = head, *delete_node, *pre;
    new_node = (Data *)malloc(sizeof(Data));
    new_node->age = val;

    if (head->age == 7)
    {

        new_node->next = head->next;
        head->next = new_node;

        return;
    }

    while (temp_head->age != 7)
    {
        printf("Inside while %d \n", temp_head->age);

        temp_head = temp_head->next;
    }
    printf("outside while %d \n", temp_head->age);

    new_node->next = temp_head->next;
    temp_head->next = new_node;

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

    insert_at_last(1);
    insert_at_last(2);
    insert_at_last(3);
    insert_at_last(4);
    insert_at_last(5);
    insert_at_last(6);
    insert_at_last(7);
    insert_at_last(8);
    insert_at_last(9);

    insert_a_node_after_seven_val_node(10756);

    // del_by_pos(2);

    // del_by_val(1);

    display();

    return 0;
}
