# CereStim SWIG Wrapper

This contains a SWIG wrapper for Blackrock Microsystems CereStim API.

## Prerequisites

* [SWIG](http://www.swig.org/download.html). In Windows, get swigwin.
* [CereStim API (scroll down on support page)](https://blackrockneurotech.com/support/)
    * Copy the extracted folder into this directory (i.e. `CereStimWrapper\CereStim-API`)
* Python
* A compiler (I think it should [match your Python version's compiler](https://wiki.python.org/moin/WindowsCompilers#Which_Microsoft_Visual_C.2B-.2B-_compiler_to_use_with_a_specific_Python_version_.3F))

## Build & Install

1. Make sure swig.exe is on your PATH.
    * via system environment variables
    * via command prompt, e.g: `set PATH=%PATH%;%HOMEPATH%\Downloads\swigwin-4.1.1\swigwin-4.1.1`
1. May need to set PYTHON_INCLUDE and PYTHON_LIB 
1. Open this directory in command prompt. (probably x64 Native Tools Command Prompt for VS 2019)
1. `swig -c++ -python -I"CereStim-API/Binaries/" cerestim/cerestim.i`
1. Switch to your Anaconda Prompt, activate an appropriate environment, and `cd` to this directory.
1. `pip install .`

## Usage

I plan to make a more featureful Python package. For now, the compiled module can be imported directly.

```Python
import cerestim
```
