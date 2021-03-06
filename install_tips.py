#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:34:43 2019

@author: luke
"""

"""
# Installation

Requirements beyond NumPy, SciPy, Matplotlib:

pip install euclid
pip install plyfile
pip install pyOpenGL

pyOpenGL GLUT issue:
    https://stackoverflow.com/questions/26700719/pyopengl-glutinit-nullfunctionerror

    Linux Users can just install glut using the following command:

    $ sudo apt-get install freeglut3-dev


Most critical, you need suitsparse for fast inversion of sparse matrices 
in order to take advantage of some of the solver forumulations:

get an up to date suitsparse [here](https://pythonhosted.org/scikit-sparse/overview.html)
    
    Installing scikit-sparse requires:

    Python
    NumPy
    SciPy
    Cython
    CHOLMOD

On Debian/Ubuntu systems, the following command should suffice:

    $ apt-get install python-scipy libsuitesparse-dev


    Then just:

    $ pip install --user scikit-sparse



"""