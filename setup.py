#!/usr/bin/env python

from __future__ import print_function;

import os
import sys
from distutils.core import setup, Extension
from subprocess import call as subpcall
from distutils.command.install import install as DistutilsInstall

setup(
   name='h3k27ac_trough',
   version='1.0',
   license="MIT",
   description='h3k27ac_trough_identification',
   author='Chen-Hao Chen',
   author_email='hyalin1127@gmail.com',
   packages=['h3k27ac_trough'],
   package_dir={'h3k27ac_trough':'h3k27ac_trough'},
)
