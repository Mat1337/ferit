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

int main(void) {
    // random seed for the number generator
    srand((unsigned int) time(NULL));

    int array[10];
    random_array(&array, 10);

    return 0;
}