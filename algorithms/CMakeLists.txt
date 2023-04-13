# set the minimum cmake version this project supports
cmake_minimum_required(VERSION 3.25)

# create the project
project(algorithms VERSION 1.0 LANGUAGES C)

# set the c language standard version
set(CMAKE_C_STANDARD 17)

# set the include directories for all the projects
include_directories(include)

# create the base library
add_library(algorithms STATIC src/timings.c include/timings.h)

# this function creates a test
function(CREATE_LAB NAME)
    # get all the c source files for the current lab
    file(GLOB files "${CMAKE_CURRENT_SOURCE_DIR}/${NAME}/*.c")

    # initialize a counter variable
    set(counter 0)

    # loop through all the source files
    foreach (file ${files})
        # and create an executable for each one
        add_executable("${NAME}_${counter}" ${file})

        # link the executable with the static library
        target_link_libraries("${NAME}_${counter}" ${PROJECT_NAME})

        # increment the counter variable
        math(EXPR counter "${counter} + 1")
    endforeach ()
endfunction()

# create all the labs here
CREATE_LAB(lab_1)
CREATE_LAB(lab_2)
CREATE_LAB(lab_3)