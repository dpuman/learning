#include <stdio.h>
int main()
{
    char ch1[] = "Dipu";
    char ch2[] = "Dipu";
    int flag = 0;

    for (int i = 0; ch1[i] != '\0' || ch2[i] != '\0'; i++)
    {
        if (ch1[i] != ch2[i])
        {
            flag = 1;
            break;
        }
    }

    if (flag == 1)
    {
        printf("Not Equal");
    }
    else
        printf("Equal");

    return 0;
}
