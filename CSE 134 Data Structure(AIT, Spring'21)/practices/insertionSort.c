#include <stdio.h>
int main()
{
    int arra[10], i, j, n, temp;
    printf("Input  no. of values in the array: \n");
    scanf("%d", &n);
    printf("Input  %d array value(s): \n", n);
    for (i = 0; i < n; i++)
        scanf("%d", &arra[i]);

    /* Insertion Sort  */
    for (i = 1; i < n; i++)
    {
        temp = arra[i];
        j = i - 1;
        while (j >= 0 && arra[j] > temp)
        {
            arra[j + 1] = arra[j];
            j--;
        }
        arra[j + 1] = temp;
    }
    printf("Sorted  Array: \n");
    for (i = 0; i < n; i++)
        printf("%d  \n", arra[i]);
}
