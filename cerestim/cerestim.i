%module cerestim
 %{
 /* Includes the header in the wrapper code */
 #include "BStimulator.h"
 %}
 #define STATIC_BSTIM_LINK
 /* Parse the header file to generate wrappers */
 %include "BStimulator.h"