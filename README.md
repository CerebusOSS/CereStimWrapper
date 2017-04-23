# CereStim SWIG Wrapper

This contains a SWIG wrapper for Blackrock Microsystems CereStim API.
cmake can be used to generate a MSVC solution or a makefile for the Python wrapper.

## Prerequisites

* [SWIG](http://www.swig.org/download.html). In Windows, get swigwin.
* [cmake](https://cmake.org/download/)
* A C++ build environment like MSVC.
* Python

## Build

1. Make sure swig.exe is on your PATH.
    * via system environment variables
    * via command prompt: `set PATH=%PATH%;E:\Tools\Misc\swigwin-3.0.12`
2. Open this directory in command prompt.
3. `mkdir build && cd build`
4. Run `cmake ..` You may need to pass in the PYTHON_LIBRARY path.
    * `cmake .. -G "Visual Studio 14 2015 Win64" -DPYTHON_LIBRARY="C:\Program Files\Python35\libs\python35.lib"`
5. Open the pycerestim.sln
6. Change the configuration from 'Debug' to 'Release'
7. Build the _cerestim target.

## Install

This is not yet implemented.

1. `pip install .`

## Usage

I plan to make a more featureful Python package. For now, the compiled module can be imported directly.

```Python
import _cerestim
```