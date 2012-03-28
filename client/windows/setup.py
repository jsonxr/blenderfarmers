from distutils.core import setup
from glob import glob

import py2exe
import os
import glob
from py2exe.build_exe import py2exe as build_exe

class MediaCollector(build_exe):
    def copy_extensions(self, extensions):
        super(MediaCollector, self).copy_extensions(extensions)

        # Create the media subdir where the
        # Python files are collected.
#        media = os.path.join('foo', 'media')
        full = os.path.join(self.collect_dir, "resources")
        if not os.path.exists(full):
            self.mkpath(full)

        # Copy the media files to the collection dir.
        # Also add the copied file to the list of compiled
        # files so it will be included in zipfile.
        for f in glob.glob('../shared/resources/*'):
            name = os.path.basename(f)
            self.copy_file(f, os.path.join(full, name))
            self.compiled_files.append(os.path.join(media, name))

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll']
mydata_files = [('resources', ['C:\\blenderfarmers/client/shared/resources/gui.xrc'])]


setup(
    options = {"py2exe": {
                          "compressed": 2,
                          "optimize": 2,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 3,
                          "dist_dir": "dist",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },
    windows=['../shared/BlenderFarmers.py'],
    data_files = mydata_files
)