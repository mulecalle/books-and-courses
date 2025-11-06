from tkinter import *
from DBHandler import deleteUser

def deleteFrame():

    FrameLeer = Toplevel()

    vars_leer = deleteFrane(FrameLeer)

    Button(FrameLeer, text='Delete', command=(lambda: seekAndDelete(vars_leer, FrameLeer))).pack()

    FrameLeer.grab_set()
    FrameLeer.focus_set()
    FrameLeer.wait_window()

def deleteFrane(root):

    formulario = Frame(root)
    formulario.pack(expand=YES)

    div0 = Frame(formulario, padx=5, pady=5, borderwidth=2, relief='groove')
    div0.pack()

    id_leer = Entry(div0)
    id_leer.config(justify=CENTER, width=40)
    id_leer.pack()

    idVar = StringVar()
    id_leer.config(textvariable=idVar)
    id_leer.bind('<Button-1>', (lambda event: clearEntry(idVar)))

    idVar.set("-- Ingrese el id --")

    return idVar

def clearEntry(arg):
    arg.set("")


def seekAndDelete(userId, root):

    textToDisplay = deleteUser(userId)
    popupMessage(textToDisplay, root)

def popupMessage(txtToDisplay, root):
    root = Toplevel()
    formulario = Frame(root)
    formulario.pack(side=TOP, expand=YES, fill=BOTH)

    Label(formulario, text=txtToDisplay, bg="gray", fg="white", justify=CENTER).pack(side=TOP, expand=YES, fill=X, anchor=W)

    formulario.grab_set()
    formulario.focus_set()
    formulario.wait_window()
