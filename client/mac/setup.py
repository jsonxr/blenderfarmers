"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app

URL:    
    http://svn.pythonmac.org/py2app/py2app/trunk/doc/index.html
    
"""

from setuptools import setup


# The file paths are in relation to the "build" directory.
# We create these from the build directory because it installs
# a bunch of *.egg files, poluting the directory we run
# the command from.
APP = ['../shared/BlenderFarmers.py']
DATA_FILES = ['../shared/resources']
OPTIONS = {
    'argv_emulation': True,
    'iconfile' : 'BlenderFarmers.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)