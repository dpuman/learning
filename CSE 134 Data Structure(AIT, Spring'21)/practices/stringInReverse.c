#include <stdio.h>

int main()
{

    char ch1[] = "Amar shonar bangla ami tomay valo bashi";

    int size = sizeof(ch1) / sizeof(ch1[0]);
    // printf("%d", size);

    for (int i = size; i >= 0; i--)
    {
        printf("%c", ch1[i]);
    }

    return 0;
}
