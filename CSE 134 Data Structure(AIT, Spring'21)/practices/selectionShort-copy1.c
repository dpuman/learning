#include <stdio.h>
int main()
{
    int arr[10];
    int i, j, N, temp;
    /* function  declaration */
    int find_max(int b[10], int k);
    void exchang(int b[10], int k);
    printf("\nInput no. of values in the array : N");
    scanf("%d", &N);
    printf("\nInput  the elements one by one: ");
    for (i = 0; i < N; i++)
    {
        scanf("%d", &arr[i]);
    }
    /* Selection sorting  begins */
    exchang(arr, N);
    printf("Sorted  array :\n");
    for (i = 0; i < N; i++)
    {
        printf("%d\n", arr[i]);
    }
}
/* function to find the maximum value */
int find_max(int b[10], int k)
{
    int max = 0, j;
    for (j = 1; j <= k; j++)
    {
        if (b[j] > b[max])
        {
            max = j;
        }
    }
    return (max);
}
void exchang(int b[10], int k)
{
    int temp, big, j;
    for (j = k - 1; j >= 1; j--)
    {
        big = find_max(b, j);
        temp = b[big];
        b[big] = b[j];
        b[j] = temp;
    }
    return;
}
