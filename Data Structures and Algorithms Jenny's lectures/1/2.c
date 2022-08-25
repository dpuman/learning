#include <stdio.h>
#include <stdlib.h>
// ARRAY DELETE
int main()
{
    int a[50], size, i, j, pos, item;
    printf("Enter size :");
    scanf("%d", &size);
    if (size < 50)
    {
        for (i = 0; i < size; i++)
        {
            scanf("%d", &a[i]);
        }
    }
    else
    {
        printf("Out of bound");
    }

    for (i = 0; i < size; i++)
    {
        printf("%d", a[i]);
    }

    printf("\nEnter position want to delete:");
    scanf("%d", &pos);

    // FOR UNSORTED ARRAY
    if (pos >= 0 || pos < size)
    {
        a[pos - 1] = a[size - 1];
    }
    else
    {
        printf("Not possible");
    }
    size--;

    printf("After Delete:");

    for (i = 0; i < size; i++)
    {
        printf("%d", a[i]);
    }

    return 0;
}