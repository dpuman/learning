#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *next;
};
typedef struct Node queue;
// Insert at last
void enque(queue *q, int data)
{
    queue *temp;
    temp = (queue *)malloc(sizeof(queue));

    temp->data = data;
    temp->next = NULL;
    while (q->next != NULL)
    {
        q = q->next;
    }
    q->next = temp;
    printf("%d is enqueued!\n", data);
}

int dequeue(queue *q)
{
    queue *temp;
    int data;
    if (q->next == NULL)
    {
        printf("Queue is empty!\n");
        return -1;
    }
    temp = q->next;
    data = temp->data;
    q->next = temp->next;
    free(temp);
    return data;
}
int main()
{
    queue *q;
    q = (queue *)malloc(sizeof(queue));
    q->next = NULL;

    enque(q, 10);
    enque(q, 5);
    enque(q, 11);

    printf("%d\n", dequeue(q));
    printf("%d\n", dequeue(q));
    printf("%d\n", dequeue(q));
    return 0;
}