from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("multiplicacion_matreces_CY.pyx"))
setup(ext_modules = exts)