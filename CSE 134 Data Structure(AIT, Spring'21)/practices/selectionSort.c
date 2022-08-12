#include <stdio.h>
int main()
{
    int arr[] = {15, 56, 12, 1, 659, 3, 83, 51, 3, 135, 0};
    int i, j, n, temp, min, idx;

    n = sizeof(arr) / sizeof(arr[0]);

    for (i = 0; i < n - 1; i++)
    {

        min = i;
        for (j = i + 1; j < n; j++)
        {

            if (arr[j] < arr[min])
            {
                min = j;
            }
        }

        if (min != i)
        {
            temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }
    }

    printf("Sorted  array :\n");
    for (i = 0; i < n; i++)
    {
        printf("%d\n", arr[i]);
    }
}
