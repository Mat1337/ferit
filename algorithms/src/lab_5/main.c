//
// Created by mat on 4/20/23.
//

#include <timings.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define RANDOM_MIN 0
#define RANDOM_MAX 1000

static void random_array(int *array, int len) {
    for (int i = 0; i < len; ++i)
        array[i] = rand() % RANDOM_MAX + RANDOM_MIN;
}

static void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

static void heapify(int *arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

void heap_sort(int *arr, int n) {
    SECTION_START_FUNC
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i >= 0; i--) {
        swap(&arr[0], &arr[i]);
        heapify(arr, i, 0);
    }
    SECTION_END_FUNC
}

static void bubble_sort(int *array, int len) {
    SECTION_START_FUNC
    for (int i = 0; i < len - 1; i++)
        for (int j = 0; j < len - i - 1; j++)
            if (array[j] > array[j + 1])
                swap(&array[j], &array[j + 1]);
    SECTION_END_FUNC
}

static void merge(int arr[], int l,
                  int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    i = 0;
    j = 0;

    k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

static void merge_sort(int *arr,
                       int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        merge_sort(arr, l, m);
        merge_sort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}

int main(void) {
    // random seed for the number generator
    srand((unsigned int) time(NULL));

    int size;
    do {
        printf("Unesi velicinu: ");
        scanf("%d", &size);
    } while (size < 0);

    /*
    int *array = (int *) calloc(sizeof(int), size);
    if (array == NULL)
        return 1;

    random_array(array, size);*/

    int array[7] = {12, 5, 4, 10, 7, 8, 11};
    size = 7;

    for (int i = 0; i < size; ++i)
        printf("%d\n", array[i]);

    heap_sort(array, size);

    printf("####################\n");

    for (int i = 0; i < size; ++i)
        printf("%d\n", array[i]);

    free(array);
    return 0;
}