#!/usr/bin/env python
import os
import distutils
from setuptools import setup, Extension, find_packages
import platform

api_dir = 'CereStim-API/Binaries'
arch = 'x64' if '64bit' in platform.architecture() else 'x86'
lib_name = 'BStimAPI' + arch
full_lib_relative = api_dir + '/' + lib_name + '.dll'
package_name = 'cerestim'

cerestim_module = Extension('cerestim._cerestim',
                            sources=['cerestim/cerestim_wrap.cxx'],
                            include_dirs=[api_dir],
                            libraries=[lib_name],
                            library_dirs=[api_dir],
                            language='c++'
                           )

setup(
    name            = package_name,
    version         = '0.1',
    author          = 'Chadwick Boulay',
    author_email    = 'chadwick.boulay@gmail.com',
    description     = 'Wrapper for Blackrock Microsystems CereStim API',
    license         = 'MIT',
    packages        = [package_name],
    ext_modules     = [cerestim_module],
    data_files      = [('Lib/site-packages/' + package_name, [full_lib_relative])]  # Copy dll into correct directory.
)
