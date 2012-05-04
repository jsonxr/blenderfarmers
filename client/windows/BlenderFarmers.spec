# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'), os.path.join(HOMEPATH,'support/useUnicode.py'), SPECPATH+'/../shared/BlenderFarmers.py'],
             pathex=['C:\\pyinstaller-1.5.1'])

a.datas += [('resources/gui.xrc', SPECPATH+'/../shared/resources/gui.xrc',  'DATA'),
            ('resources/blenderfarmers.ico', SPECPATH+'/../shared/resources/blenderfarmers.ico',  'DATA'),
            ]

pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'BlenderFarmers.exe'),
          debug=False,
          strip=False,
          upx=True,
          icon=SPECPATH+"/../shared/resources/blenderfarmers.ico",
          console=False )

app = BUNDLE(exe, name=os.path.join('dist', 'BlenderFarmers.app'))

