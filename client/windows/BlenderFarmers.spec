# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), '\\blenderfarmers\\client\\shared\\BlenderFarmers.py'],
             pathex=['C:\\pyinstaller-1.5.1'])
             
a.datas += [('resources/gui.xrc', 'c:\\blenderfarmers\\client\\shared\\resources\\gui.xrc',  'DATA'),
            ('blenderfarmers.ico', 'c:\\blenderfarmers\\client\\windows\\blenderfarmers.ico',  'DATA')
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
          icon="c:\\blenderfarmers\\client\\windows\\blenderfarmers.ico,15",
          console=False )

app = BUNDLE(exe, name=os.path.join('dist', 'BlenderFarmers.exe.app'))

