# This CMakeLists is no longer used.
# I am keeping it around as a resource on how to use cmake with SWIG
# mkdir build && cd build
# cmake .. -G "Visual Studio 14 2015 Win64" -DPYTHON_LIBRARY="C:\Program Files\Python36\libs\python36.lib"
# Open the pycerestim.sln
# Change configuration from Debug to Release
# Build the _cerestim target.
# Open python and `import _cerestim`


cmake_minimum_required(VERSION 3.8)
project(pycerestim VERSION 0.0.1)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/../pycerestim)

FIND_PACKAGE(SWIG REQUIRED)
INCLUDE(${SWIG_USE_FILE})

if( CMAKE_SIZEOF_VOID_P EQUAL 8 )
    set(sys_arch "x64")
else()
    set(sys_arch "x86")
endif()

FIND_PACKAGE(PythonLibs)
INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_PATH})

INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR})

set(CERESTIM_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../CereStim API/")
FIND_LIBRARY(CERESTIM_LIBRARIES
    BStimAPI${sys_arch}
    PATHS ${CERESTIM_PATH})
INCLUDE_DIRECTORIES(${CERESTIM_PATH})

SET(CMAKE_SWIG_FLAGS "")

SET_SOURCE_FILES_PROPERTIES(cerestim.i PROPERTIES CPLUSPLUS ON)
#SET_SOURCE_FILES_PROPERTIES(cerestim.i PROPERTIES SWIG_FLAGS "-includeall")
SWIG_ADD_LIBRARY(cerestim
                 LANGUAGE python
                 SOURCES cerestim.i
                 )
SWIG_LINK_LIBRARIES(cerestim ${PYTHON_LIBRARIES} ${CERESTIM_LIBRARIES})

set_target_properties(_cerestim PROPERTIES LIBRARY_OUTPUT_DIRECTORY_RELEASE ${CMAKE_LIBRARY_OUTPUT_DIRECTORY})

# Copy dll
add_custom_command(TARGET _cerestim POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${CERESTIM_PATH}/BStimAPI${sys_arch}.dll"
        $<TARGET_FILE_DIR:_cerestim>
)
# Copy include file over too for reference.
add_custom_command(TARGET _cerestim POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${CERESTIM_PATH}/BStimulator.h"
        $<TARGET_FILE_DIR:_cerestim>
)

#execute_process(
#    COMMAND python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"
#    OUTPUT_VARIABLE PYTHON_SITE_PACKAGES OUTPUT_STRIP_TRAILING_WHITESPACE)
#install(TARGETS _cerestim DESTINATION ${PYTHON_SITE_PACKAGES})
#install(FILES ${CMAKE_BINARY_DIR}/src/cerestim.py DESTINATION ${PYTHON_SITE_PACKAGES})