#include <stdio.h>

#include <stdlib.h>

typedef struct Data
{
    int age;
    struct Data *next;
} Data;

Data *head;

void PUSH(int val)
{

    Data *temp = (Data *)malloc(sizeof(Data));
    temp->age = val;
    temp->next = NULL;

    temp->next = head;
    head = temp;
    return;
}

int POP()
{
    Data *temp_head = head;
    head = temp_head->next;
    int val = temp_head->age;
    free(temp_head);
    return val;
}

int TOP()
{
    Data *temp_head = head;
    int return_val;

    while (temp_head != NULL)
    {
        temp_head = temp_head->next;
    }
    return_val = temp_head->age;
    return return_val;
}

int main()
{

    int x;
    PUSH(1);
    PUSH(2);
    PUSH(3);
    PUSH(4);

    x = POP();

    printf("%d", x);

    return 0;
}
