#include <stdio.h>
#include <stdlib.h>
typedef struct Data
{
    int num;
    struct Data *next;
    struct Data *prev;
} Data;

Data *head, *tail;

int n[] = {1, 2, 3, 4, 5, 6, 7};

void insert_at_left(int pos, int val)
{

    Data *temp_head = head;

    Data *node = (Data *)malloc(sizeof(Data));
    node->num = val;
    node->next = NULL;
    node->prev = NULL;

    printf("%d", pos);
    while (temp_head->num != pos)
    {
        if (temp_head->next == NULL)
        {
            printf("Cant find tthe nimber");
        }

        temp_head = temp_head->next;
    }

    if (temp_head->prev == NULL || temp_head == head)
    {

        temp_head->prev = node;
        node->next = temp_head;
        head = temp_head;
    }

    temp_head->prev->next = node;
    node->prev = temp_head->prev;

    temp_head->prev = node;
    node->next = temp_head;
}
void insert_at_right(int pos, int val)
{
    Data *temp_head = head;

    Data *node = (Data *)malloc(sizeof(Data));
    node->num = val;
    node->next = NULL;
    node->prev = NULL;

    while (temp_head->num != pos)
    {
        temp_head = temp_head->next;
    }

    if (temp_head->next == NULL || temp_head == tail)
    {
        temp_head->next = node;
        node->prev = temp_head;
        tail = temp_head;
    }

    temp_head->next->prev = node;
    node->next = temp_head->next;

    temp_head->next = node;
    node->prev = temp_head;
}
void display()
{
    printf("Hello");
    Data *temp_head = head;

    while (temp_head != NULL)
    {

        printf("%d\n", temp_head->num);
        temp_head = temp_head->next;
    }

    return;
}

int main()
{

    int i;
    int size = sizeof(n) / sizeof(n[0]);

    Data *node = (Data *)malloc(sizeof(Data));
    node->num = n[0];
    node->next = NULL;
    node->prev = NULL;
    head = node;
    tail = node;

    for (i = 0; i < size; i++)
    {
        printf("%d", n[i]);

        insert_at_left(n[i], n[2 * i + 1]);
        insert_at_right(n[i], n[2 * i + 2]);
    }

    display();

    return 0;
}