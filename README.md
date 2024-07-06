# CereStim SWIG Wrapper

This contains a SWIG wrapper for Blackrock Microsystems CereStim API.

## Downloads

Head to the [releases page](https://github.com/CerebusOSS/CereStimWrapper/releases) to see if there is a release for you.

## Build

If there isn't a pre-made release for you, you can build it yourself. Blackrock only provides binaries for Windows x64 and Windows x86, so you can only target those platforms.

### Prerequisites

* [SWIG](http://www.swig.org/download.html). Download swigwin and extract the archive.
* [CereStim API (scroll down on support page)](https://blackrockneurotech.com/support/)
    * Copy the extracted folder into this directory (i.e. `CereStimWrapper\CereStim-API`)
* Python
* A compiler (I think it should [match your Python version's compiler](https://wiki.python.org/moin/WindowsCompilers#Which_Microsoft_Visual_C.2B-.2B-_compiler_to_use_with_a_specific_Python_version_.3F))

### Build & Install

1. Open this directory in command prompt. (probably x64 Native Tools Command Prompt for VS 2019)
2. Make sure swig.exe is on your PATH.
    * via system environment variables
    * via command prompt, e.g: `set PATH=%PATH%;%HOMEDRIVE%\%HOMEPATH%\Downloads\swigwin-4.2.1\swigwin-4.2.1`
3. May need to set PYTHON_INCLUDE and PYTHON_LIB 
4. `swig -c++ -python -I"CereStim-API/Binaries/" cerestim/cerestim.i`
5. Switch to your Anaconda Prompt, activate an appropriate environment, and `cd` to this directory.
6. `pip install .` or `pip wheel .` to build only the wheel.

## Usage

The compiled module can be imported directly.
Read the Blackrock-provided documentation for more information on the API

```Python
import cerestim
```

You can also find a package that uses this wrapper at https://github.com/CerebusOSS/CereStimDBS
