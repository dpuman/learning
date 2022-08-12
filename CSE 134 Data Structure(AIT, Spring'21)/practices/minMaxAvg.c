#include <stdio.h>
#include <stdlib.h>
typedef struct Data
{
    int num;
    struct Data *next;
} Data;

Data *head;

void link_list_at_first(int val)
{
    Data *node = (Data *)malloc(sizeof(Data));
    node->num = val;
    node->next = NULL;

    node->next = head;

    head = node;

    return;
}

void display()
{
    Data *temp_head = head;

    while (temp_head != NULL)
    {
        printf("%d\n", temp_head->num);
        temp_head = temp_head->next;
    }

    return;
}

int min()
{
    Data *temp_head = head;
    int min;

    min = temp_head->num;

    while (temp_head != NULL)
    {
        if (temp_head->num < min)
        {
            min = temp_head->num;
        }
        temp_head = temp_head->next;
    }
    return min;
}

float average()
{
    Data *temp_head = head;
    int total = 0;
    float avg, sum = 0.0;

    while (temp_head != NULL)
    {
        total++;
        sum += temp_head->num;
        temp_head = temp_head->next;
    }

    avg = sum / total;

    return avg;
}
int main()
{
    link_list_at_first(5);
    link_list_at_first(2);
    link_list_at_first(1);
    link_list_at_first(4);
    link_list_at_first(5);

    display();
    // printf("HEllo");

    printf("MIN %d\n", min());
    printf("AVERAGE %.2f\n", average());

    return 0;
}