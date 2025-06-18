# -*- mode: python ; coding: utf-8 -*-

import os
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# تحديد المسار الأساسي
block_cipher = None
pathex = [os.path.abspath('.')]

# جمع البيانات والملفات المطلوبة
datas = []

# إضافة ملفات القوالب
if os.path.exists('templates'):
    datas.append(('templates', 'templates'))

# إضافة الملفات الثابتة
if os.path.exists('static'):
    datas.append(('static', 'static'))

# إضافة ملفات التكوين
config_files = ['config.py', 'models.py']
for file in config_files:
    if os.path.exists(file):
        datas.append((file, '.'))

# إضافة ملفات قاعدة البيانات (إذا كانت موجودة)
if os.path.exists('instance'):
    datas.append(('instance', 'instance'))

# جمع بيانات Flask وReportLab
try:
    datas += collect_data_files('flask')
    datas += collect_data_files('reportlab')
    datas += collect_data_files('arabic_reshaper')
    datas += collect_data_files('bidi')
except:
    pass

# الوحدات المخفية المطلوبة
hiddenimports = [
    'flask',
    'flask_sqlalchemy',
    'sqlalchemy',
    'sqlalchemy.ext.declarative',
    'sqlalchemy.orm',
    'reportlab',
    'reportlab.pdfgen',
    'reportlab.lib',
    'reportlab.platypus',
    'arabic_reshaper',
    'bidi',
    'bidi.algorithm',
    'openpyxl',
    'xlsxwriter',
    'weasyprint',
    'pdfkit',
    'PIL',
    'PIL.Image',
    'tkinter',
    'tkinter.ttk',
    'tkinter.messagebox',
    'threading',
    'webbrowser',
    'socket',
    'contextlib',
    'subprocess',
    'datetime',
    'json',
    'os',
    'sys',
    'time',
    'io'
]

# إضافة وحدات Flask الفرعية
try:
    hiddenimports += collect_submodules('flask')
    hiddenimports += collect_submodules('flask_sqlalchemy')
    hiddenimports += collect_submodules('sqlalchemy')
    hiddenimports += collect_submodules('reportlab')
except:
    pass

# تحليل الملف الرئيسي
a = Analysis(
    ['main.py'],
    pathex=pathex,
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'IPython',
        'jupyter',
        'notebook',
        'PyQt5',
        'PyQt6',
        'PySide2',
        'PySide6',
        'wx'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# إزالة الملفات المكررة
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# إنشاء ملف exe واحد
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SAM_PRO',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # إخفاء نافذة وحدة التحكم
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
    version_file='version_info.txt' if os.path.exists('version_info.txt') else None
)

# إنشاء مجلد التوزيع (اختياري)
# coll = COLLECT(
#     exe,
#     a.binaries,
#     a.zipfiles,
#     a.datas,
#     strip=False,
#     upx=True,
#     upx_exclude=[],
#     name='SAM_PRO'
# )
