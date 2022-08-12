#include <stdio.h>

int partition(int arr[], int lb, int ub)
{

    int pivot = arr[lb];
    int start = lb;
    int end = ub;
    int temp;
    while (start < end)
    {
        while (arr[start] <= pivot)
        {
            start++;
        }
        while (arr[end] > pivot)
        {
            end--;
        }
        if (start < end)
        {
            temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
        }
    }
    temp = arr[lb];
    arr[lb] = arr[end];
    arr[end] = temp;

    return end;
}

void quick_sort(int arr[], int lb, int ub)
{
    int loc;
    if (lb < ub)
    {
        loc = partition(arr, lb, ub);
        quick_sort(arr, lb, ub - 1);
        quick_sort(arr, lb + 1, ub);
    }
}
int main()
{
    int arr[] = {15, 56, 12, 1, 659, 3, 83, 51, 3, 135, 0}, lb, ub, i;
    void quick_sort(int arr[], int, int);

    int n = sizeof(arr) / sizeof(arr[0]);

    lb = 0;
    ub = n - 1;
    quick_sort(arr, lb, ub);

    printf("\nThe quick sorted array is:  ");
    for (i = 0; i < n; i++)
        printf(" %d", arr[i]);
    printf("\n");
}
