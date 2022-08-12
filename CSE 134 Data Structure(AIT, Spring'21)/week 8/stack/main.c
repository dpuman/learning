#include <stdio.h>
#include <stdlib.h>
int stack_arr[50], top = -1;

void PUSH(int val)
{
    if (top == 49)
    {
        printf("FULL MEMORY");
        return;
    }
    stack_arr[++top] = val;
    return;
}

int POP()
{
    if (top == -1)
    {
        printf("Empty MEMORY");
        return;
    }

    int return_data = stack_arr[top--];
    return return_data;
}

int TOP()
{
    return stack_arr[top];
}

int main()
{
    int x;
    PUSH(5);

    x = POP();

    printf("%d", x);

    return 0;
}
