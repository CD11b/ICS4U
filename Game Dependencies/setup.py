import os
from cx_Freeze import setup, Executable

executables = [
    Executable('ReRun.py')
]

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python36\tcl\tk8.6'

setup(name='ReRUn',
      version='0.1',
      description='game',
      options = {"build_exe": {"packages": ["pygame", "pkg_resources"], "include_files": ["EnvImages", "IntroGifs", "Music", "OutroGifs", "Story"]}},
      executables =executables
      )
