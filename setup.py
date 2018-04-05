from cx_Freeze import setup, Executable

executables = [
    Executable('versionify.py')
]

setup(name='versionify',
      version='0.1',
      description='A simple application to create backups of files',
      executables=executables
      )