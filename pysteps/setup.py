# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.extension import Extension

try:
    import numpy
except ImportError:
    raise RuntimeError(
        "Numpy required to pior running the package installation\n" +
        "Try installing it with:\n" +
        "$> pip install numpy")

#_vet_extension_arguments = dict(extra_compile_args=['-fopenmp'],
#                                include_dirs=[numpy.get_include()],
#                                language='c',
#                                extra_link_args=['-fopenmp'])
#
#try:
#    from Cython.Build.Dependencies import cythonize
#
#    _vet_lib_extension = Extension(str("pysteps.motion._vet"),
#                                   sources=[str('pysteps/motion/_vet.pyx')],
#                                   **_vet_extension_arguments)
#
#    external_modules = cythonize([_vet_lib_extension])
#
#except ImportError:
#    _vet_lib_extension = Extension(str(str("pysteps.motion._vet")),
#                                   sources=[str('pysteps/motion/_vet.c')],
#                                   **_vet_extension_arguments)
#    external_modules = [_vet_lib_extension]

requirements = ['numpy',
                'attrdict', 'jsmin', 'scipy', 'matplotlib',
                'jsonschema']

setup(
    name='pysteps',
    version='0.2',
    packages=find_packages(),
    license='LICENSE',
    include_package_data=True,
    description='Python framework for short-term ensemble prediction systems',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'],
#    ext_modules=external_modules,
    setup_requires=requirements,
    install_requires=requirements
)
