#include <stdio.h>

void bubble_sort(int *x, int n)
{
    int i, j, temp, flag;
    for (i = 0; i < n - 1; i++)
    {
        flag = 0;
        for (j = 0; j < n - 1 - i; j++)
        {
            if (x[j] > x[j + 1])
            {
                flag = 1;
                temp = x[j];
                x[j] = x[j + 1];
                x[j + 1] = temp;
            }
        }
        if (flag == 0)
        {
            break;
        }
    }
}

int main()
{
    int x[] = {15, 56, 12, -21, 1, 659, 3, 83, 51, 3, 135, 0};
    int n = sizeof x / sizeof x[0];
    int i;
    for (i = 0; i < n; i++)
        printf("%d%s", x[i], i == n - 1 ? "\n" : " ");
    bubble_sort(x, n);
    for (i = 0; i < n; i++)
        printf("%d%s", x[i], i == n - 1 ? "\n" : " ");
    return 0;
}

// IN best Case O(n) in worse case O(n^2) cos: (n-1) (n-1)
