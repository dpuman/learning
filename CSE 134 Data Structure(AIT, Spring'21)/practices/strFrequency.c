#include <stdio.h>

int main()
{

    char ch1[] = "Amar shonar bangla ami tomay valo bashi";

    int size = sizeof(ch1) / sizeof(ch1[0]), count = 0;
    // printf("%d", size);

    for (int i = 0; ch1[i] != '\0'; i++)
    {
        char a[] = "a";

        if (a[0] == ch1[i])
        {
            count++;
        }

        printf("%c", ch1[i]);
    }

    printf("%d", count);

    return 0;
}
