import os
from setuptools import Extension, setup


def get_compile_definitions(likwid_header_path: str):
    define_macros = []

    nvmon = os.getenv("LIKWID_NVMON", default="0")
    if nvmon != "0":
        define_macros.append(("LIKWID_NVMON", None))

    with open(likwid_header_path) as file:
        for line in file:
            if line.startswith("#define LIKWID_VERSION"):
                major, release, minor = line.split()[-1].strip('"').split(".")

                define_macros.extend([
                    ("LIKWID_MAJOR", major),
                    ("LIKWID_RELEASE", release),
                    ("LIKWID_MINOR", minor)
                ])

    return define_macros



# assuming LIKWID_PREFIX has this structure
# ├── bin
# │   ├── likwid-bench
# │   ├── ...
# │   └── likwid-topology
# ├── include
# │   ├── likwid.h
# │   └── likwid-marker.h
# ├── lib
# │   ├── ...
#     └── liblikwid.so.5.5
likwid_prefix = os.getenv(key="LIKWID_PREFIX", default="/usr/local")
print(f"Searching for likwid at {likwid_prefix}/")


include_dir = os.path.join(likwid_prefix, "include")
library_dir = os.path.join(likwid_prefix, "lib")
likwid_header_path = os.path.join(include_dir, "likwid.h")
macros = get_compile_definitions(likwid_header_path)


setup(
    ext_modules=[
        Extension(
            name="pylikwid",
            sources=["pylikwid.c"],
            include_dirs=[include_dir],
            library_dirs=[library_dir],
            libraries=["likwid"],
            runtime_library_dirs=[library_dir],
            define_macros=macros
        )
    ]
)
