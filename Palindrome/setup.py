from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("Palindrome_CY.pyx"))
setup(ext_modules = exts)