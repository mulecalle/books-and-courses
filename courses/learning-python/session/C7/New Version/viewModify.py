from tkinter import *
from DBHandler import deleteUser
from DBHandler import userExist
from DBHandler import grabDataFromDB
from DBHandler import DBModify
campos = ('nombre', 'edad', 'sueldo', 'trabajo')
variables = [None] * 4

def modifyFrame():

    FrameLeer = Toplevel()

    vars_leer = ModifyFrame(FrameLeer)

    Button(FrameLeer, text='Search', command=(lambda: seekUser(vars_leer, FrameLeer))).pack()

    FrameLeer.grab_set()
    FrameLeer.focus_set()
    FrameLeer.wait_window()

def ModifyFrame(root):

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


def seekUser(userID, root):

    FrameLeer = Toplevel()

    if userExist(userID):

        newValues = detailsFrame(FrameLeer, userID)

        DBModify(newValues, userID)

        root.destroy()

    else:

        popupMessage(FrameLeer, "Cannot find the "+userID.get()+" user ID", root)


def popupMessage(toplvl, txtToDisplay, root):

    form = Frame(toplvl)
    form.pack(side=TOP, expand=YES, fill=BOTH)

    Label(form, text=txtToDisplay, bg="gray", fg="white", justify=CENTER).pack(side=TOP, expand=YES, fill=X, anchor=W)

    form.grab_set()
    form.focus_set()
    form.wait_window()

def detailsFrame(Tplvl, userID):

    aUser = grabDataFromDB(userID)

    form = Frame(Tplvl)

    div1 = Frame(form, width=100)
    div2 = Frame(form, padx=7, pady=2)

    lab1 = Label(div1, width=10, text=campos[0])
    lab2 = Label(div1, width=10, text=campos[1])
    lab3 = Label(div1, width=10, text=campos[2])
    lab4 = Label(div1, width=10, text=campos[3])

    ent1 = Entry(div2, width=30, relief=SUNKEN)
    ent2 = Entry(div2, width=30, relief=SUNKEN)
    ent3 = Entry(div2, width=30, relief=SUNKEN)
    ent4 = Entry(div2, width=30, relief=SUNKEN)

    lab1.pack(side=TOP)
    lab2.pack(side=TOP)
    lab3.pack(side=TOP)
    lab4.pack(side=TOP)

    ent1.pack(side=TOP, fill=X)
    ent2.pack(side=TOP, fill=X)
    ent3.pack(side=TOP, fill=X)
    ent4.pack(side=TOP, fill=X)

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()

    var1.trace("w", lambda name, index, mode, var=var1: callback(name, 0, mode, var1))
    var2.trace("w", lambda name, index, mode, var=var2: callback(name, 1, mode, var2))
    var3.trace("w", lambda name, index, mode, var=var3: callback(name, 2, mode, var3))
    var4.trace("w", lambda name, index, mode, var=var4: callback(name, 3, mode, var4))

    ent1.config(textvariable=var1)
    ent2.config(textvariable=var2)
    ent3.config(textvariable=var3)
    ent4.config(textvariable=var4)

    var1.set(aUser.nombre)
    var2.set(aUser.edad)
    var3.set(aUser.sueldo)
    var4.set(aUser.trabajo)

    form.pack(fill=X)

    Button(form, text='Update', command=(lambda: save(Tplvl))).pack(side=BOTTOM)

    div1.pack(side=LEFT)
    div2.pack(side=RIGHT, expand=YES, fill=X)

    form.grab_set()
    form.focus_set()
    form.wait_window()

    return variables


def callback(name, index, mode, var):

    variables[index] =  str(var.get())


def save(detailsFrame):
    detailsFrame.destroy()