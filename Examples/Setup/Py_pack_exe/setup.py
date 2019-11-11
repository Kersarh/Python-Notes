# coding: utf-8

from cx_Freeze import setup, Executable
import sys
base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable(
        'main.py',  # Главный файл программы
        targetName='run.exe',  # Имя exe файла
        base=base,
        icon='app.ico')
]

# Исключения
excludes = [
    'bz2', 'hashlib', 'lzma', 'socket', 'ssl', 'pyexpat', 'select',
    'unicodedata'
]

# Добавить модули
add_modul = []

# Добавить модули в zip
zip_include_packages = [
    'collections', 'encodings', 'importlib', 'email', 'html', 'http',
    'logging', 'pydoc_data', 'unittest', 'urllib', 'xml', 'bz2', 'hashlib',
    'lzma', 'socket', 'ssl', 'pyexpat', 'select', 'unicodedata'
] + add_modul

# Включаемые файлы и папки проэкта
include_files = ['data', 'file.py']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
        'include_files': include_files,
    }
}

setup(name='Python_Profgamm',
      version='0.1',
      description='Программа написанная на Python!',
      executables=executables,
      options=options)
