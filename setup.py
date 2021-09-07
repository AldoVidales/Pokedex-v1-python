import cx_Freeze
from tkinter import * 
from PIL import  Image,ImageTk
import  requests
from io import BytesIO
import  pokebase as pb
import  sys

base = None 
if sys.platform == "win32": 
    base = "Win32GUI"


executables = [cx_Freeze.Executable("main.py",icon="icono.ico",base = base)]

cx_Freeze.setup(
    name="Pokedex",
    version="1.0",
    
    author="Aldo Vidales",
    author_email="profesional@aldovidales.com",
    options={"build_exe": {"packages":["PIL","pokebase","tkinter","requests","io","dbm.gnu","dbm.dumb","dbm.ndbm"],
                           "include_files":["logo.png","icono.ico"]}},
    executables = executables
    #hola soy aldo

    )