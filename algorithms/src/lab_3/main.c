//
// Created by mat on 4/13/23.
//
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include "timings.h"

typedef struct {
    uint32_t stack[256];
    uint32_t size;
} stack_t;

void stack_push(stack_t *stack, uint32_t value) {
    stack->stack[stack->size] = value;
    stack->size++;
}

bool stack_empty(stack_t *stack) {
    return stack->size == 0;
}

uint32_t stack_pop(stack_t *stack) {
    uint32_t value = stack->stack[stack->size - 1];
    stack->size--;
    return value;
}

uint32_t povrh(uint32_t n, uint32_t m) {
    if (m == n || n == 1 || m == 0)
        return 1;
    return povrh(n - 1, m - 1) + povrh(n - 1, m);
}

int main(void) {
    uint32_t value;
    do {
        printf("Enter a number: ");
        scanf("%ld", (long *) &value);
    } while (value < 0);

    stack_t n_stack = {0};
    stack_t m_stack = {0};

    stack_push(&n_stack, value);
    stack_push(&m_stack, value / 2);

    section_start("povrh_stack");
    uint32_t povrh = 0;
    do {
        uint32_t n = stack_pop(&n_stack);
        uint32_t m = stack_pop(&m_stack);

        if (m == n || n == 0) {
            povrh++;
        } else {
            stack_push(&n_stack, m - 1);
            stack_push(&n_stack, m - 1);
            stack_push(&m_stack, n - 1);
            stack_push(&m_stack, n);
        }
    } while (stack_empty(&n_stack) == false);
    section_start("povrh_stack");

    printf("result: %d\n", povrh);

    return 0;
}