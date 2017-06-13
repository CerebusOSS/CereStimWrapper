# CereStim SWIG Wrapper

This contains a SWIG wrapper for Blackrock Microsystems CereStim API.
cmake can be used to generate a MSVC solution or a makefile for the Python wrapper.

## Prerequisites

* [SWIG](http://www.swig.org/download.html). In Windows, get swigwin.
* [CereStim API](http://blackrockmicro.com/technical-support/software-downloads/) extracted into this directory (i.e. `CereStimWrapper\CereStim API`)
* Python
* A compiler (I think it should [match your Python version's compiler](https://wiki.python.org/moin/WindowsCompilers#Which_Microsoft_Visual_C.2B-.2B-_compiler_to_use_with_a_specific_Python_version_.3F))

## Build & Install

1. Make sure swig.exe is on your PATH.
    * via system environment variables
    * via command prompt: `set PATH=%PATH%;D:\Tools\Misc\swigwin-3.0.12`
1. May need to set PYTHON_INCLUDE and PYTHON_LIB 
1. Open this directory in command prompt.
1. `swig -c++ -python -py3 -I"CereStim API/" cerestim/cerestim.i`
1. `pip3 install .`

## Usage

I plan to make a more featureful Python package. For now, the compiled module can be imported directly.

```Python
import cerestim
```