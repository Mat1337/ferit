cmake_minimum_required(VERSION 3.25)
project(algorithms C)

set(CMAKE_C_STANDARD 17)

include_directories(include)

add_library(utilities STATIC src/timings.c include/timings.h)

add_executable(lab_1_zad_1 lab_1/zad_1.c)
target_link_libraries(lab_1_zad_1 utilities)

add_executable(lab_2_zad_1 lab_2/zad_1.c)
target_link_libraries(lab_2_zad_1 utilities)