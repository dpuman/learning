#include <stdio.h>
#include <stdlib.h>

int queue_arr[50], front, back;
front = -1;
back = -1;

void enqueue(int val)
{
    queue_arr[++back] = val;
    if (front == -1)
        front++;
    return;
}

int dequeue()
{
    int return_val = queue_arr[front];
    front++;

    return return_val;
}

int main()
{
    enqueue(10);
    enqueue(20);
    int value = dequeue();

    printf("%d\n", value);
    return 0;
}
