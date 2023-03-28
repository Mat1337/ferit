#include <timings.h>
#include <stdio.h>

time_t current_time;

const char *section_start(const char *section) {
    current_time = clock();
    return section;
}

void section_end(const char *section) {
    printf("function '%s' took '%ld' ms to execute\n", section, (clock() - current_time));
}