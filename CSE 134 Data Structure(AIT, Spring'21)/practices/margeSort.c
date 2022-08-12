#include <stdio.h>

void marge(int arr[], int lb, int mid, int ub)
{
    int i = lb, j = mid + 1, k = lb;
    int arr2[ub];

    while (i <= mid && j <= ub)
    {

        if (arr[i] <= arr[j])
        {
            arr2[k] = arr[i];
            i++;
            k++;
        }
        else
        {
            arr2[k] = arr[j];
            j++;
            k++;
        }
    }
    if (i > mid)
    {
        while (j <= ub)
        {
            arr2[k] = arr[j];
            j++;
            k++;
        }
    }
    else
    {
        while (i <= mid)
        {
            arr2[k] = arr[i];
            i++;
            k++;
        }
    }

    for (int i = 0; i < ub; i++)
    {
        printf("%d\n", arr2[i]);
    }

    return;
}

void marge_sort(int arr[], int lb, int ub)
{
    if (lb < ub)
    {
        int mid = (lb + ub) / 2;

        marge_sort(arr, lb, mid);
        marge_sort(arr, mid + 1, ub);
        marge(arr, lb, mid, ub);
    }
}
int main()
{
    int arr[] = {15, 56, 12, 1, 659, 3, 83, 51, 3, 135, 0}, lb, ub, i;

    int n = sizeof(arr) / sizeof(arr[0]);

    lb = 0;
    ub = n - 1;
    marge_sort(arr, lb, ub);
}
