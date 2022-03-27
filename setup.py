import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
include_files=['yt.jpg','ytskip.jpg','images']
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"],'include_files':include_files}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="YT Setup",
    author="Aakash",
    version="1.0.0",
    description="Automatic YouTube Add Skip",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py",icon='yt.ico', base=base)],
)