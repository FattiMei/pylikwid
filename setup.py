from setuptools import Extension, setup


setup(
    ext_modules=[
        Extension(
            name="pylikwid",
            sources=["pylikwid.c"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            libraries=["likwid"],
            runtime_library_dirs=["/usr/local/lib"],
            define_macros=[
              ("LIKWID_MAJOR", "5"),
              ("LIKWID_RELEASE", "5"),
              ("LIKWID_MINOR", "1"),
            ]
        )
    ]
)
