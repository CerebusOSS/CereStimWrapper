%module cerestim
 %{
 /* Includes the header in the wrapper code */
 #include "BStimulator.h"
 %}
 #define STATIC_BSTIM_LINK
 %include "std_vector.i"
 %include "typemaps.i"
 %template() std::vector<int>;
 %apply std::vector<int> *OUTPUT { std::vector<UINT32> & device_serial_nums };
 
 /* Parse the header file to generate wrappers */
 %include "BStimulator.h"