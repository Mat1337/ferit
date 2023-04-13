/*
    Zadatak 1
*/

#include <stdlib.h>
#include <stdio.h>

// custom utility
#include <timings.h>

static void gen_arr(float *array, int count, float min, float max) {
    SECTION_START_FUNC
    for (int i = 0; i < count; ++i)
        array[i] = (int) (((rand() / (float) RAND_MAX) * (max - min)) + min);
    SECTION_END_FUNC
}

static int sekv_pret(float *array, int count, float x) {
    SECTION_START_FUNC
    int index = -1;
    for (int i = 0; i < count; ++i) {
        if (array[i] == x) {
            index = i;
            break;
        }
    }
    SECTION_END_FUNC
    return index;
}

static void sort(float *array, int count) {
    SECTION_START_FUNC
    for (int step = 0; step < count - 1; ++step) {
        for (int i = 0; i < count - step - 1; ++i) {
            if (array[i] > array[i + 1]) {
                float temp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = temp;
            }
        }
    }
    SECTION_END_FUNC
}

//////////////////////////////////////////////////
//
//  Binary search
//
//////////////////////////////////////////////////

int bin_pret_range(float *array, int x, int low, int high) {
    if (high >= low) {
        int mid = low + (high - low) / 2;

        if (array[mid] == x)
            return mid;

        if (array[mid] > x)
            return bin_pret_range(array, x, low, mid - 1);

        return bin_pret_range(array, x, mid + 1, high);
    }

    return -1;
}

static int bin_pret(float *array, int count, float x) {
    SECTION_START_FUNC
    int index = bin_pret_range(array, x, 0, count);
    SECTION_END_FUNC
    return index;
}

//////////////////////////////////////////////////

int main(void) {
    time_t t1, t2;

    // random seed for the generator
    srand((unsigned int) time(NULL));

    // constraints for the random generator
    static float min = 10;
    static float max = 20;

    int size;
    do {
        printf("Enter size: ");
        scanf("%d", &size);
    } while (size < 0);

    float *array = (float *) calloc(size, sizeof(float));

    gen_arr(array, size, min, max);
    sekv_pret(array, size, 15);
    sort(array, size);
    bin_pret(array, size, 15);

    free(array);
    return 0;
}