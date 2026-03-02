Tentative installation procedure for the likwid python API

# Prerequisites
  * `likwid` must be installed on the system. For more information, consult the [official repository](https://github.com/RRZE-HPC/likwid).
  * you need the python development files (something similar to `python3.13-dev` on apt)
  * `pip`
  * (*recommended*) a python virtual environment


# Installation

```bash
git clone --depth 1 https://github.com/FattiMei/pylikwid
cd pylikwid

LIKWID_PREFIX=/usr/local pip install .
```

`LIKWID_PREFIX` should be where likwid was installed. If you don't define the environment variable, the install script will look in `/usr/local`


# Examples
>You always have to use ``likwid-perfctr`` to program the hardware performance counters and specify the CPUs that should be measured.

```bash
likwid-perfctr -C 0 -g L3 -m python tests/testmarker.py
```
