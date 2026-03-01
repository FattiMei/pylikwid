Tentative installation procedure for the likwid python API

# Prerequisites
`likwid` must be installed on the system. For more information, consult the [official repository](https://github.com/RRZE-HPC/likwid).


# likwid workflow
>DISCLAIMER: this is almost certainly incorrect, but it's a good starting point.

A user could use likwid as a profiling tool for a target program. In particular he can select:
  * on which socket/core the target program must be executed
  * which performance counter to measure

this usage profiles the entire application which is not desirable

## Marker API
Allows the user runtime control of the profiling. The original application is modified to make use of the marker API defined in `<likwid.h>` which are a set of data structures and functions. The application must be linked with the likwid shared object.

## Standalone executions
I'm not sure if an application that makes use of the marker API must also be invocated through `likwid-perfctr` to register correctly the performance counters.


# pylikwid workflow
It seems that the authors wanted to make the marker API accessible from python. They built `pylikwid.c` with the idea of building the python package `pylikwid` via the `distutils` (now deprecated in favour of `setuptools`)


# Python installation
On a system that:
  * has a working likwid installation
  * the command `python -c "import distutils"` works

the following commands successfully install the `pylikwid` package:
```bash
# I'm relying on the automatic discovery of the LIWKID installation path
python setup.py build_ext
python setup.py install --user
```
