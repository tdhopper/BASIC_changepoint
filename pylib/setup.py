import numpy
from setuptools import setup, Extension
from distutils.sysconfig import get_python_inc

exec(open("BASIC_changepoint/_version.py").read())

ext_modules = [
    Extension(
        "BASIC_changepoint._c_funcs",
        sources=[
            "BASIC_changepoint/py_extension.cpp",
            "../src/base.cpp",
            "../src/inference_procedures.cpp",
            "../src/bernoulli_model.cpp",
            "../src/laplace_scale_model.cpp",
            "../src/normal_mean_model.cpp",
            "../src/normal_mean_var_model.cpp",
            "../src/normal_var_model.cpp",
            "../src/poisson_model.cpp",
        ],
        include_dirs=[get_python_inc(), numpy.get_include()],
        extra_compile_args=["-std=c++11", "-I/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/v1"]

    )
]

setup(
    name="BASIC_changepoint",
    version="0.0.1",
    description="BASIC (Bayesian Analysis of SImultaneous Changepoints)",
    packages=["BASIC_changepoint"],
    ext_modules=ext_modules,
)
