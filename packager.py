import sys
from cx_Freeze import setup, Executable

setup(
    name = "Crony",
    version = "1.1",
    description = "PC Cleaning and Optimizing Tool",
    executables = [Executable("Crony.py", base = "Win32GUI",icon="Logo.ico")])
