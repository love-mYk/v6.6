# -*- mode: python ; coding: utf-8 -*-
# WellCorrelator v6.5 PyInstaller 单文件打包配置

block_cipher = None

a = Analysis(
    ['v6_6.py'],
    pathex=[],
    binaries=[],
    datas=[
        # 如果有资源文件在这里添加，比如：
        # ('resources/', 'resources/', 'DATA'),
    ],
    hiddenimports=[
        'PyQt6',
        'PyQt6.QtCore',
        'PyQt6.QtGui',
        'PyQt6.QtWidgets',
        'pyqtgraph',
        'pyqtgraph.graphicsItems.PlotItem',
        'numpy',
        'pandas',
        'lasio',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'tkinter',
        'IPython',
        'notebook',
        'jupyter',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='WellCorrelator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,        # True=带黑窗口，False=纯GUI
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,            # 可换成 .ico 路径
)