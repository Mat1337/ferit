//
// Created by matko on 3/28/23.
//

#include <stdio.h>
#include <stdlib.h>

#include <timings.h>

#define RANDOM_MIN 0
#define RANDOM_MAX 1000

typedef struct entry {
    int value;
    struct entry *next;
} entry_t;

/////////////////////////////////////////////////////
//
//  Array
//
/////////////////////////////////////////////////////

static int *create_array(int size) {
    SECTION_START_FUNC
    int *array = (int *) calloc(size, sizeof(int));
    if (array == NULL)
        fprintf(stderr, "Failed to allocate memory for the array\n");
    SECTION_END_FUNC
    return array;
}

static int seq_search_array(const int *array, int size, int x) {
    SECTION_START_FUNC
    int index = -1;
    for (int i = 0; i < size; ++i) {
        if (array[i] == x) {
            index = i;
            break;
        }
    }
    SECTION_END_FUNC
    return index;
}

/////////////////////////////////////////////////////
//
//  Linked list
//
/////////////////////////////////////////////////////

static entry_t *create_entry(int value) {
    entry_t *entry = (entry_t *) malloc(sizeof(entry_t));
    if (entry == NULL)
        return NULL;

    entry->value = value;
    entry->next = NULL;

    return entry;
}

static void create_list(entry_t **list, int *array, int size) {
    SECTION_START_FUNC
    entry_t *last = *list;
    for (int i = 0; i < size; i++) {
        entry_t *entry = create_entry(array[i]);
        if (entry == NULL)
            continue;

        if (last != NULL)
            last->next = entry;
        else
            *list = entry;

        last = entry;
    }
    SECTION_END_FUNC
}

static int seq_search_list(entry_t *head, int x) {
    SECTION_START_FUNC
    int index = -1, count = 0;
    entry_t *iterator = head;
    while (iterator != NULL) {
        if (iterator->value == x) {
            index = count;
            break;
        }
        iterator = iterator->next;
        count++;
    }
    SECTION_END_FUNC
    return index;
}

static void free_list(entry_t *list) {
    entry_t *iterator = list;
    while (iterator != NULL) {
        entry_t *temp = iterator;
        iterator = iterator->next;
        free(temp);
    }
}

/////////////////////////////////////////////////////

int main(void) {
    // seed for random number generation
    srand((unsigned int) time(NULL));

    int size;
    do {
        printf("Enter the size of array: ");
        scanf("%d", &size);
    } while (size < 0);

    int *array = create_array(size);
    if (array == NULL)
        return 1;

    // populate the array with values
    for (int i = 0; i < size; ++i)
        array[i] = (int) ((((float) rand() / (float) RAND_MAX) * (RANDOM_MAX - RANDOM_MIN)) + RANDOM_MIN);

    entry_t *head = NULL;
    create_list(&head, array, size);

    int seq_array_search = seq_search_array(array, size, -10);
    int seq_list_search = seq_search_list(head, -10);

    printf("seq_array_search = %d\n", seq_array_search);
    printf("seq_list_search = %d\n", seq_list_search);

    free(array);
    free_list(head);
    return 0;
}