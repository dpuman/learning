#include <stdio.h>
#include <stdlib.h>
// ARRAY Delete Sorted
int main()
{
    int a[50], size, i, j, pos;
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

    printf("Enter position want to delete");
    scanf("%d", &pos);

    // FOR SORTED ARRAY O(size-position)
    if (pos >= 0 || pos <= size)
    {
        for (i = pos - 1; i < size - 1; i++)
        {
            a[i] = a[i + 1];
        }
        size -= 2;
    }
    else
    {
        printf("Not possibke");
    }

    for (i = 0; i <= size; i++)
    {
        printf("%d", a[i]);
    }

    return 0;
}