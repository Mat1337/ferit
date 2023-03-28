//
// Created by matko on 3/28/23.
//

#ifndef ALGORITHMS_TIMINGS_H
#define ALGORITHMS_TIMINGS_H

#include <time.h>

const char* section_start(const char* section);
void section_end(const char* section);

#define SECTION_START_FUNC  const char* __current_section__ = section_start(__FUNCTION__);
#define SECTION_END_FUNC    section_end(__current_section__);

#endif //ALGORITHMS_TIMINGS_H
