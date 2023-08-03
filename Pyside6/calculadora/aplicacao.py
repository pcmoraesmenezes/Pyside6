import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Se você quiser uma janela sem console no Windows

executables = [
    Executable("main.py", base=base, icon="files/icon.png")
]

setup(
    name="calculadora",
    version="1.0",
    description="Minha Calculadora",
    executables=executables
)
