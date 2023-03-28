/*
    Zadatak 1
*/

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

static void gen_arr(float* array, int count, float min, float max) {
    for(int i = 0; i < count; ++i) 
        array[i] = (int)(((rand() / (float)RAND_MAX) * (max - min)) + min);
}

static int sekv_pret(float *array, int count, float x) {
    for(int i = 0; i < count; ++i) 
        if (array[i] == x)
            return i;
    return -1;
}

static void sort(float* array, int count) {
  for (int step = 0; step < count - 1; ++step) {
    for (int i = 0; i < count - step - 1; ++i) {
      if (array[i] > array[i + 1]) {
        float temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
      }
    }
  }
}

//////////////////////////////////////////////////
//
//  Binary search
//
//////////////////////////////////////////////////

int bin_pret_range(float* array, int x, int low, int high) {
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

static int bin_pret(float* array, int count, float x) {
    return bin_pret_range(array, x, 0, count);
}

//////////////////////////////////////////////////

int main(void) {
    time_t t1, t2;

    // random seed for the generator
    srand((unsigned int)time(NULL));

    // constraints for the random generator
    static float min = 10;
    static float max = 20;

    int size;
    do {
        printf("Enter size: ");
        scanf("%d", &size);
    } while(size < 0);

    float* array = (float*)calloc(size, sizeof(float));
    
    t1 = clock();
    gen_arr(array, size, min, max);
    t2 = clock();
    printf("gen_arr=%dms\n", t2 - t1);

    t1 = clock();
    printf("sekv_pret=%d\n", sekv_pret(array, size, 15));
    t2 = clock();
    printf("sekv_pret=%dms\n", t2 - t1);

    t1 = clock();
    sort(array, size);
    t2 = clock();
    printf("sort=%dms\n", t2 - t1);

    t1 = clock();
    printf("bit_pret=%d\n", bin_pret(array, size, 15));
    t2 = clock();
    printf("bit_pret=%dms\n", t2 - t1);

    free(array);
    return 0;
}