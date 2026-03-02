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
