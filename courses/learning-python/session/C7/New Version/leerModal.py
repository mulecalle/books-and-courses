from tkinter import *
from leer import CrearFormLeer
from DBHandler import grabDataFromDB

def lee(userId, root):

    root = Toplevel()
    formulario = Frame(root)
    formulario.pack(side=TOP, expand=YES, fill=BOTH)

    txtToDisplay = grabDataFromDB(userId)

    Label(formulario, text=txtToDisplay, bg="gray", fg="white", justify=CENTER).pack(side=TOP, expand=YES, fill=X, anchor=W)

    formulario.grab_set()
    formulario.focus_set()
    formulario.wait_window()

def leer():

    FrameLeer = Toplevel()

    vars_leer = CrearFormLeer(FrameLeer)

    Button(FrameLeer, text='Leer', command=(lambda: lee(vars_leer, FrameLeer))).pack()

    FrameLeer.grab_set()
    FrameLeer.focus_set()
    FrameLeer.wait_window()