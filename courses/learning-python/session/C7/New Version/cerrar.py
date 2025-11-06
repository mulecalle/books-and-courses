from tkinter import *
from tkinter.messagebox import askokcancel

def Cerrar():
    consulta = askokcancel('Cerrar', "¿Desea abandonar la aplicación?")
    if consulta:
        quit()