# -*- mode: python -*-
a = Analysis(['rpchm.py'],
             pathex=['D:\\work\\rpchm-py'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)

a.datas += [('HTML Help Workshop/hhc.exe', 'HTML Help Workshop/hhc.exe',  'DATA'),
 ('HTML Help Workshop/itcc.dll', 'HTML Help Workshop/itcc.dll',  'DATA'),]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'rpchm.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=True , resources=[])

