#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[50], size, i, j, num, pos;
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

    printf("Enter data want to insert");
    scanf("%d", &num);

    printf("Enter the position");
    scanf("%d", &pos);
    // FOR SORTED ARRAY
    if (pos >= 0 || pos <= size + 1)
    {
        for (i = size - 1; i > pos - 1; i--)
        {
            a[i + 1] = a[i];
        }
        a[pos] = num;
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