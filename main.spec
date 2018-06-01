# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\GihanUOM\\Desktop\\CCTV'],
             binaries=[],
             datas=[('templates', 'templates'), ('static', 'static'), ('Caffe_Data', 'Caffe_Data'), ('Data_Access', 'Data_Access'), ('Heat', 'Heat'), ('Region_drawing', 'Region_drawing'), ('Sample_Videos', 'Sample_Videos'), ('snapshots', 'snapshots')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
